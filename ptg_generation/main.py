import json
import os
import base64
from google import genai
from google.genai import types

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def ptg_generate(image_dir, content):
    image_files = []

    # ambil file PNG
    files = os.listdir(image_dir)
    png_files = [f for f in files if f.endswith(".png")]
    png_file_names = [f.split(".")[0] for f in png_files]

    # masukkan daftar nama file PNG ke prompt
    content = content.format(node_id_list=json.dumps(png_file_names))

    for file in png_files:
        with open(os.path.join(image_dir, file), "rb") as f:
            image_files.append(f.read())  # raw bytes

    # Initialize Gemini client
    client = genai.Client()
    

    # prepare prompt gemini
    contents = [types.Part(text=content)]

    # masukin image ke prompt
    for img_bytes in image_files:
        contents.append(
            types.Part(inline_data=types.Blob(mime_type="image/png", data=img_bytes))
        )

    # generate pake gemini-2.0-flash-exp
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
    )

    res_text = response.text.strip()

    # Hapus ```json atau ``` jika ada
    if res_text.startswith("```"):
        res_lines = res_text.split("\n")
        if res_lines[0].startswith("```"):
            res_lines = res_lines[1:]
        if res_lines[-1].startswith("```"):
            res_lines = res_lines[:-1]
        res_text = "\n".join(res_lines)

    # Pastikan JSON valid
    try:
        res_json = json.loads(res_text)
    except json.JSONDecodeError as e:
        print("Error parsing JSON dari output LLM:", e)
        res_json = {}  # fallback

    return res_json


if __name__ == "__main__":
    picture_folder = "../images"
    ptg_prompt_path = "PTG_Prompt.txt"
    ptg_result_path = "PTG_Result.json" 
    
    # baca prompt
    with open(ptg_prompt_path, "r", encoding="utf-8") as f:
        ptg_prompt = f.read()

    # generate PTG
    res_json = ptg_generate(picture_folder, ptg_prompt)

    # tampilkan hasil
    print(json.dumps(res_json, indent=2))

    # simpan ke file .json
    with open(ptg_result_path, "w", encoding="utf-8") as f:
        json.dump(res_json, f, indent=2)

    print(f"Hasil disimpan ke {ptg_result_path}")
