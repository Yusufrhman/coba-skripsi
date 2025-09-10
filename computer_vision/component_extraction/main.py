import os
import shutil
import numpy as np
import cv2
from PIL import Image
import torch
from lang_sam import LangSAM


def clear_folder(folder_path: str):
    """Hapus semua isi folder (jika ada)."""
    if not os.path.exists(folder_path):
        return
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Gagal hapus {file_path}: {e}")


def process_images(input_dir: str, output_root: str, text_prompt: str):
    """
    Proses semua gambar PNG di input_dir menggunakan LangSAM
    Struktur hasil:
      result/
        └── <nama_gambar>/
             ├── original.png
             └── split_img/
                  ├── 1.png
                  ├── 2.png
                  └── position.txt
    """
    if not os.path.exists(input_dir):
        raise FileNotFoundError(f"Folder input '{input_dir}' tidak ditemukan.")

    # Bersihkan folder output agar fresh
    clear_folder(output_root)
    os.makedirs(output_root, exist_ok=True)

    # Load model LangSAM
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Running on: {device}")
    model = LangSAM(device=device)

    # Ambil semua file PNG
    files = [f for f in os.listdir(input_dir) if f.endswith(".png")]
    if not files:
        print(f"Tidak ada file PNG di {input_dir}")
        return

    for file in files:
        imgname = os.path.splitext(file)[0]
        img_path = os.path.join(input_dir, file)

        # Buat folder khusus untuk gambar ini
        img_root = os.path.join(output_root, imgname)
        split_dir = os.path.join(img_root, "split_img")
        os.makedirs(split_dir, exist_ok=True)

        # Copy image original ke dalam folder gambar
        shutil.copy(img_path, os.path.join(img_root, "original.png"))

        # Buka gambar
        image_pil = Image.open(img_path).convert("RGB")

        # Prediksi pakai LangSAM
        results = model.predict([image_pil], [text_prompt])
        if not results:
            print(f"Tidak ada hasil prediksi untuk {file}")
            continue

        result = results[0]
        masks = result.get("masks", [])
        boxes = result.get("boxes", [])

        # Simpan koordinat box
        with open(os.path.join(split_dir, "position.txt"), "w") as pos_file:
            for i, mask in enumerate(masks):
                # pastikan mask numpy array
                if isinstance(mask, torch.Tensor):
                    mask = mask.cpu().numpy()

                # gambar asli
                image = cv2.imread(img_path)  # BGR
                h, w = image.shape[:2]

                # bikin RGBA
                transparent = np.zeros((h, w, 4), dtype=np.uint8)
                transparent[:, :, :3] = image
                transparent[:, :, 3] = mask.astype(np.uint8) * 255

                # Crop sesuai bounding box
                if i < len(boxes):
                    x0, y0, x1, y1 = map(int, boxes[i])
                    cropped = transparent[y0:y1, x0:x1]
                    box_list = boxes[i].tolist()
                    pos_file.write(" ".join(map(str, box_list)) + "\n")
                else:
                    x, y, bw, bh = cv2.boundingRect(mask.astype(np.uint8))
                    cropped = transparent[y : y + bh, x : x + bw]

                # Simpan crop RGBA
                crop_path = os.path.join(split_dir, f"{i+1}.png")
                Image.fromarray(cropped, "RGBA").save(crop_path)

        print(f"Selesai: {file}")

    print(f"Semua hasil disimpan di: {output_root}")


if __name__ == "__main__":
    input_folder = "../../images"  # folder input
    output_root = "../results"  # folder output
    text_prompt = "icon.button.text"

    process_images(input_folder, output_root, text_prompt)
