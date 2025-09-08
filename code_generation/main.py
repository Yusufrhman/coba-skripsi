import json
import os
import time
import logging
import base64
import re
import glob
from pathlib import Path
from google import genai
from google.genai import types

# ====================== Path Configuration ======================
# Path konfigurasi utama - sudah disesuaikan dengan struktur folder yang diminta
PTG_PATH = "../ptg_generation/PTG_Result.json"
COMPONENT_TYPE_BASE_PATH = "../component_analysis/results"  # Base path untuk component type
IMAGES_PATH = "../images"
PROMPT_TEMPLATES_PATH = "./prompt"  # Path ke folder template prompt
OUTPUT_PATH = "./result"  # Path output hasil kode

# ====================== Konfigurasi ======================
# Konfigurasi khusus untuk generator UI berbasis Svelte
UI_TYPE = "Svelte"  # Target UI framework
SAVE_TYPE = "svelte"  # Ekstensi file output
ENTRY_FUNC_NAME = "App"  # Nama entry component utama
EXTEND_NAME = "_page"  # Suffix untuk setiap komponen halaman
NAV_CODE_TEMPLATE = ["goto('{nav_id}')", "push('{nav_id}')"]  # Template navigasi

# Logging konfigurasi
logging.basicConfig(
    level=logging.INFO,
    filename="svelte_code_generate.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s \n %(message)s",
)


# ====================== Utility ======================
def encode_image(image_path: str) -> bytes:
    """Membaca gambar dan mengembalikan byte array (PNG)."""
    try:
        with open(image_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"Image file not found: {image_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading image {image_path}: {str(e)}")
        raise


def clean_code_response(response: str) -> str:
    """Menghapus wrapper kode (``` ... ```) dari respons model."""
    if response.startswith("```"):
        lines = response.splitlines()
        if len(lines) > 2:
            return "\n".join(lines[1:-1])  # ambil isi di tengah
    return response


def save_response(filename, response):
    """Menyimpan hasil kode yang dihasilkan ke file .svelte."""
    try:
        os.makedirs(OUTPUT_PATH, exist_ok=True)
        file_path = os.path.join(OUTPUT_PATH, f"{filename}.{SAVE_TYPE}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response)
        logging.info(f"Successfully saved: {file_path}")
    except Exception as e:
        logging.error(f"Error saving file {filename}: {str(e)}")
        raise


# ====================== Data Loader ======================
def get_page_list():
    """Mengambil daftar ID halaman dari file PTG.json."""
    try:
        with open(PTG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [node["id"] for node in data["N"]]
    except FileNotFoundError:
        logging.error(f"PTG file not found: {PTG_PATH}")
        raise
    except KeyError as e:
        logging.error(f"Invalid PTG format - missing key: {e}")
        raise
    except Exception as e:
        logging.error(f"Error reading PTG file: {str(e)}")
        raise


def get_navigation_list(page_name):
    """Mengambil daftar halaman tujuan navigasi dari halaman tertentu."""
    try:
        with open(PTG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        results = [
            item
            for item in data["E"]
            if item.get("from") in [page_name, "any", "*"]  # edge valid
        ]
        return [r["to"] for r in results if r["to"] != page_name]
    except Exception as e:
        logging.error(f"Error getting navigation list for {page_name}: {str(e)}")
        raise


def get_component_type(page_name):
    """Mengambil tipe komponen untuk halaman tertentu."""
    # Path baru: ../component_analysis/nama_image/nama_image_type.txt
    type_file_path = os.path.join(
        COMPONENT_TYPE_BASE_PATH, page_name, f"{page_name}_type.txt"
    )

    try:
        with open(type_file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        return content
    except FileNotFoundError:
        logging.error(f"Component type file not found: {type_file_path}")
        raise
    except Exception as e:
        logging.error(f"Error reading component type for {page_name}: {str(e)}")
        raise


def build_prompt(page_name, prompt_type="Component", sequence=1, **kwargs):
    """Membangun prompt sesuai jenisnya (Component, Navigation, Refine)."""
    try:
        # Baca data komponen dan PTG
        if page_name:  # Hanya untuk prompt Component
            component_type = get_component_type(page_name)
        else:
            component_type = ""

        with open(PTG_PATH, "r", encoding="utf-8") as f:
            ptg_data = json.load(f)

        page_list = get_page_list()

        # Prompt untuk generate komponen halaman
        if prompt_type == "Component":
            navigation_list = get_navigation_list(page_name)
            prompt_file = "FirstPrompt.txt" if sequence == 1 else "SubPrompt.txt"

            prompt_file_path = os.path.join(PROMPT_TEMPLATES_PATH, prompt_file)
            with open(prompt_file_path, "r", encoding="utf-8") as f:
                template = f.read()
            return template.format(
                UItype=UI_TYPE,
                node_id=page_name,
                page_list=page_list,
                navigation_list=navigation_list,
                component_type=component_type,
                PTG=ptg_data,
            )

        # Prompt untuk generate navigasi utama
        elif prompt_type == "Navigation":
            prompt_file_path = os.path.join(
                PROMPT_TEMPLATES_PATH, "PTG2NavigationPrompt.txt"
            )
            with open(prompt_file_path, "r", encoding="utf-8") as f:
                template = f.read()
            return template.format(UItype=UI_TYPE, PTG=ptg_data, page_list=page_list)

        # Prompt untuk refine kode navigasi
        elif prompt_type == "Refine":
            prompt_file_path = os.path.join(PROMPT_TEMPLATES_PATH, "RefineCodePrompt.txt")
            with open(prompt_file_path, "r", encoding="utf-8") as f:
                template = f.read()
            component_path = os.path.join(
                OUTPUT_PATH, f"{page_name}{EXTEND_NAME}.{SAVE_TYPE}"
            )
            with open(component_path, "r", encoding="utf-8") as f:
                page_code = f.read()
            return template.format(
                node_id=page_name,
                implemented_ids=kwargs.get("implemented_ids", []),
                not_implemented_ids=kwargs.get("not_implemented_ids", []),
                page_code=page_code,
            )

        return ""

    except Exception as e:
        logging.error(f"Error building prompt for {page_name}: {str(e)}")
        raise


# ====================== Interaksi Gemini ======================
def send_prompt_to_gemini(client, prompt: str, image_path: str = "") -> str:
    """Mengirim prompt + optional image ke model Gemini dan kembalikan hasilnya."""
    try:
        contents = [types.Part(text=prompt)]

        # Jika ada gambar, encode dan sertakan
        if image_path and os.path.exists(image_path):
            img_bytes = encode_image(image_path)
            contents.append(
                types.Part(
                    inline_data=types.Blob(mime_type="image/png", data=img_bytes)
                )
            )

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=contents,
        )
        return clean_code_response(response.text.strip())
    except Exception as e:
        logging.error(f"Error communicating with Gemini: {str(e)}")
        raise


# ====================== Cek & Refine Navigasi ======================
def check_navigation_implementation(page_name):
    """Cek navigasi mana yang sudah/tidak diimplementasikan di file komponen."""
    try:
        navigation_list = get_navigation_list(page_name)
        code_path = os.path.join(OUTPUT_PATH, f"{page_name}{EXTEND_NAME}.{SAVE_TYPE}")

        with open(code_path, "r", encoding="utf-8") as f:
            code_content = f.read()

        implemented_ids, not_implemented_ids = [], []
        for nav_id in navigation_list:
            implemented = False
            # Cek apakah template navigasi sudah ada di kode
            for template in NAV_CODE_TEMPLATE:
                if template.format(nav_id=nav_id) in code_content:
                    implemented_ids.append(nav_id)
                    implemented = True
                    break
            if not implemented:
                not_implemented_ids.append(nav_id)

        logging.info(f"[{page_name}] Implemented IDs: {implemented_ids}")
        logging.info(f"[{page_name}] Not Implemented IDs: {not_implemented_ids}")
        return implemented_ids, not_implemented_ids

    except Exception as e:
        logging.error(f"Error checking navigation for {page_name}: {str(e)}")
        return [], []


def refine_navigation(client, page_name, implemented_ids, not_implemented_ids):
    """Refine kode navigasi sampai maksimal 3 iterasi atau semua terimplementasi."""
    max_iterations, iteration = 3, 0

    while not_implemented_ids and iteration < max_iterations:
        try:
            logging.info(
                f"[{page_name}] Refining navigation - iteration {iteration + 1}"
            )

            refine_prompt = build_prompt(
                page_name,
                prompt_type="Refine",
                implemented_ids=implemented_ids,
                not_implemented_ids=not_implemented_ids,
            )
            response = send_prompt_to_gemini(client, refine_prompt)
            save_response(f"{page_name}{EXTEND_NAME}", response)

            implemented_ids, not_implemented_ids = check_navigation_implementation(
                page_name
            )
            iteration += 1

        except Exception as e:
            logging.error(f"Error refining navigation for {page_name}: {str(e)}")
            break

    return implemented_ids, not_implemented_ids


# ====================== Validation Functions ======================
def validate_paths():
    """Validasi keberadaan path dan file yang diperlukan."""
    errors = []

    # Cek PTG file
    if not os.path.exists(PTG_PATH):
        errors.append(f"PTG file tidak ditemukan: {PTG_PATH}")

    # Cek folder images
    if not os.path.exists(IMAGES_PATH):
        errors.append(f"Folder images tidak ditemukan: {IMAGES_PATH}")
    else:
        png_files = glob.glob(os.path.join(IMAGES_PATH, "*.png"))
        if not png_files:
            errors.append(f"Tidak ada file PNG di folder: {IMAGES_PATH}")

    # Cek folder component analysis
    if not os.path.exists(COMPONENT_TYPE_BASE_PATH):
        errors.append(
            f"Folder component analysis tidak ditemukan: {COMPONENT_TYPE_BASE_PATH}"
        )

    # Cek folder prompt templates
    if not os.path.exists(PROMPT_TEMPLATES_PATH):
        errors.append(
            f"Folder prompt templates tidak ditemukan: {PROMPT_TEMPLATES_PATH}"
        )

    return errors


# ====================== Main Flow ======================
def generate_components():
    """Generate seluruh komponen halaman berdasarkan path yang dikonfigurasi."""
    try:
        # Validasi path terlebih dahulu
        validation_errors = validate_paths()
        if validation_errors:
            print("ERROR: Ditemukan masalah dengan path konfigurasi:")
            for error in validation_errors:
                print(f"  - {error}")
            return False

        client = genai.Client()

        # Ambil semua file PNG dari folder gambar
        png_files = glob.glob(os.path.join(IMAGES_PATH, "*.png"))
        page_sequence = 0

        print(f"Ditemukan {len(png_files)} file gambar untuk diproses...")

        # Proses setiap halaman berdasarkan gambar
        for png_file in png_files:
            page_sequence += 1
            page_name = os.path.splitext(os.path.basename(png_file))[0]

            print(
                f"[{page_sequence}/{len(png_files)}] Generating {page_name} component..."
            )

            try:
                # Bangun prompt untuk halaman
                prompt = build_prompt(page_name, "Component", page_sequence)
                response = send_prompt_to_gemini(client, prompt, png_file)

                # Simpan hasil kode
                print(f"----------{page_name} code generated----------")
                logging.info(f"----------{page_name} code:----------\n{response}")
                save_response(f"{page_name}{EXTEND_NAME}", response)

                # Cek dan refine navigasi
                implemented_ids, not_implemented_ids = check_navigation_implementation(
                    page_name
                )
                if not_implemented_ids:
                    print(f"  Refining navigation for {page_name}...")
                    refine_navigation(
                        client, page_name, implemented_ids, not_implemented_ids
                    )

                print(f"  Successfully saved {page_name}")

            except Exception as e:
                print(f"  ERROR processing {page_name}: {str(e)}")
                logging.error(f"Error processing {page_name}: {str(e)}")
                continue

            time.sleep(2)  # jeda antar request

        # Generate komponen App utama
        print("Generating main App component...")
        try:
            navigation_prompt = build_prompt("", "Navigation")
            app_response = send_prompt_to_gemini(client, navigation_prompt)

            logging.info(f"=========App.svelte code:=========\n{app_response}\n")
            save_response(ENTRY_FUNC_NAME, app_response)
            print("App component generated successfully!")

        except Exception as e:
            print(f"ERROR generating App component: {str(e)}")
            logging.error(f"Error generating App component: {str(e)}")

        return True

    except Exception as e:
        print(f"FATAL ERROR: {str(e)}")
        logging.error(f"Fatal error in generate_components: {str(e)}")
        return False


# ====================== Entry Point ======================
if __name__ == "__main__":
    print("Starting Svelte code generation...")
    print(f"Configuration:")
    print(f"  PTG Path: {PTG_PATH}")
    print(f"  Component Types: {COMPONENT_TYPE_BASE_PATH}")
    print(f"  Images Path: {IMAGES_PATH}")
    print(f"  Prompts Path: {PROMPT_TEMPLATES_PATH}")
    print(f"  Output Path: {OUTPUT_PATH}")
    print("-" * 50)

    start_time = time.time()
    success = generate_components()

    if success:
        print(f"\nGeneration completed successfully!")
        print(f"Total time: {time.time() - start_time:.2f}s")
        print(f"Results saved to: {OUTPUT_PATH}")
    else:
        print(f"\nGeneration failed! Check the error messages above.")
        print(f"Check log file: svelte_code_generate.log")

    print("-" * 50)
