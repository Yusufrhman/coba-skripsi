import json
import os
from google import genai
from google.genai import types
import re
import base64


def to_camel_case(s: str) -> str:
    """Convert string like 'my_image.png' to 'MyImage'"""
    s = re.sub(r"[^a-zA-Z0-9]", " ", s)  # replace non-alphanum with space
    parts = s.split()
    return "".join(word.capitalize() for word in parts)


def encode_image(path: str) -> bytes:
    """Return raw bytes of an image (PNG)."""
    with open(path, "rb") as f:
        return f.read()


def get_pages(ptg_path: str):
    print(ptg_path)
    data = json.load(open(ptg_path, "r", encoding="utf-8"))
    return [node["id"] for node in data["N"]]


def get_navigations(ptg_path: str, page_name: str):
    print(ptg_path)
    data = json.load(open(ptg_path, "r", encoding="utf-8"))
    results = [
        item
        for item in data["E"]
        if (item.get("from") == page_name) or (item.get("from") in ["any", "*"])
    ]
    return [result["to"] for result in results if result["to"] != page_name]


def save_response(prompt_response: str, file_path: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # bikin semua parent folder

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(prompt_response)

    print(f"File saved: {file_path}")


def create_prompt(
    page_name,
    ptg_path,
    type="screen",
):
    with open(ptg_path, "r", encoding="utf-8") as file:
        ptg = json.load(file)

    if type == "screen":
        screen_prompt_path = "./prompt/screen_prompt.txt"
         # component_type_path
        component_type_path = f"../computer_vision/results/{page_name}/component_analysis/{page_name}_type.txt"
        with open(component_type_path, "r", encoding="utf-8") as file:
            component_type = file.read()
        with open(screen_prompt_path, encoding="utf-8") as file:
            screen_prompt = file.read()
            prompt = screen_prompt.format(
                node_id=page_name, component_type=component_type, PTG=ptg
            )
    elif type == "navigation":
        navigation_prompt_path = "./prompt/navigation_prompt.txt"
        with open(navigation_prompt_path, "r", encoding="utf-8") as file:
            navigation_prompt = file.read()
        page_list = get_pages(ptg_path)
        prompt = navigation_prompt.format(PTG=ptg, page_list=page_list)
    return prompt


def sendPromptToGemini(prompt, encoded_img=[]):
    client = genai.Client()
    contents = [types.Part(text=prompt)]
    if len(encoded_img) > 0:
        for img in encoded_img:
            contents.append(
                types.Part(inline_data=types.Blob(mime_type="image/png", data=img))
            )

    response = client.models.generate_content(
        model="gemini-2.5-pro",
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
    return res_text


# Code generation logic goes here
if __name__ == "__main__":
    ptg_path = "../ptg_generation/PTG_Result.json"
    image_path = "../images"
    print(get_pages(ptg_path))

    files = os.listdir(image_path)
    png_files = [f for f in files if f.endswith(".png")]
    navigation_prompt = create_prompt(page_name="", ptg_path=ptg_path, type="navigation")
    navigation_response = sendPromptToGemini(navigation_prompt)
    save_response(navigation_response, "./result/App.svelte")
    
    for png_file in png_files:
        name = png_file.split(".")[0]
        screen_prompt = create_prompt(name, ptg_path, type="screen")
        print(f"Processing {name} ...")
        encoded_img = encode_image(os.path.join(image_path, png_file))
        response = sendPromptToGemini(screen_prompt, [encoded_img])
        file_path = "./result/pages/" + f"{to_camel_case(name)}Page.svelte"
        save_response(response, file_path)
        print(f"Done for {name}")
