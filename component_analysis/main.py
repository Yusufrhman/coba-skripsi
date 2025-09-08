import os
import shutil
from pathlib import Path
from google import genai
from google.genai import types


# ========= Utility =========
def encode_image(path: Path) -> bytes:
    """Return raw bytes of an image (PNG)."""
    with open(path, "rb") as f:
        return f.read()


def copy_file(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def chunked(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# ========= Core Processing =========
def split2type(
    image_input_dir: Path, image_name: str, prompt: str, batch_size: int = 10
) -> tuple[str, Path]:
    """
    Kirim original screenshot + split komponen ke Gemini per batch,
    lalu gabungkan hasil respon.
    """
    image_folder = image_input_dir / image_name

    original_img_path = image_folder / "original.png"
    split_img_dir = image_folder / "split_img"
    position_path = split_img_dir / "position.txt"

    # ambil semua split komponen
    split_pngs = []
    if split_img_dir.exists():
        split_pngs = sorted(
            [f for f in split_img_dir.iterdir() if f.suffix == ".png"],
            key=lambda x: int(x.stem) if x.stem.isdigit() else x.stem,
        )

    # init client Gemini
    client = genai.Client()

    all_responses = []

    for batch in chunked(split_pngs, batch_size):
        image_files = []

        # Original selalu ikut
        if original_img_path.exists():
            image_files.append(encode_image(original_img_path))

        # Tambahkan komponen batch ini
        for f in batch:
            image_files.append(encode_image(f))

        # prepare content
        contents = [types.Part(text=prompt)]
        for img_bytes in image_files:
            contents.append(
                types.Part(
                    inline_data=types.Blob(mime_type="image/png", data=img_bytes)
                )
            )

        # panggil model
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=contents,
        )
        all_responses.append(response.text.strip())

    # gabungkan hasil jadi satu string
    return "\n\n".join(all_responses), position_path


# ========= Main =========
if __name__ == "__main__":
    # path input hasil ekstraksi komponen
    image_input_dir = Path("../component_extraction/result")
    output_folder = Path("./results")

    prompt_path = Path("./prompt.txt")

    with open(prompt_path, "r", encoding="utf-8") as f:
        split2type_prompt = f.read()

    # loop semua folder image_name di image_input_dir
    for image_folder in image_input_dir.iterdir():
        if not image_folder.is_dir():
            continue

        image_name = image_folder.name
        print(f"Processing {image_name} ...")

        component_type, pos_before = split2type(
            image_input_dir, image_name, split2type_prompt, batch_size=10
        )

        # simpan hasil type ke /results/{image_name}
        app_output_dir = output_folder / image_name
        app_output_dir.mkdir(parents=True, exist_ok=True)

        out_type_path = app_output_dir / f"{image_name}_type.txt"
        out_type_path.write_text(component_type, encoding="utf-8")

        # copy posisi
        if pos_before.exists():
            pos_after = app_output_dir / f"{image_name}_position.txt"
            copy_file(pos_before, pos_after)

        print(f"Finished {image_name}")
