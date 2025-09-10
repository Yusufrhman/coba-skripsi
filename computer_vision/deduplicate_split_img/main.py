import os
import shutil


class Component:
    def __init__(self, id, x_min, y_min, x_max, y_max):
        self.id = id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.children = []

    def is_parent_of(self, other):
        return (
            self.x_min <= other.x_min
            and self.y_min <= other.y_min
            and self.x_max >= other.x_max
            and self.y_max >= other.y_max
        )

    def __repr__(self):
        return f"Component({self.id}, {self.x_min}, {self.y_min}, {self.x_max}, {self.y_max})"


def build_tree(components):
    roots = []
    for current in components:
        placed = False
        for potential_parent in components:
            if potential_parent != current and potential_parent.is_parent_of(current):
                potential_parent.children.append(current)
                placed = True
                break
        if not placed:
            roots.append(current)
    return roots


def print_tree(node, level=0):
    indent = " " * (level * 4)
    print(f"{indent}- Component {node.id}")
    for child in node.children:
        print_tree(child, level + 1)


def main(txt_file):
    components = []
    with open(txt_file, "r") as file:
        for i, line in enumerate(file):
            x_min, y_min, x_max, y_max = map(float, line.strip().split())
            components.append(Component(i + 1, x_min, y_min, x_max, y_max))

    tree = build_tree(components)
    root_list = [root.id for root in tree]
    return tree, root_list


def copy_images_and_text(list_of_nums, dir1, dir2, text_file, output_text_file):
    if not os.path.exists(dir2):
        os.makedirs(dir2)

    with open(text_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(output_text_file, "w", encoding="utf-8") as output_file:
        file_cnt = 0
        for filename in os.listdir(dir1):
            if filename.endswith(".png") and filename.split(".")[0] in map(
                str, list_of_nums
            ):
                file_cnt += 1
                new_filename = f"{file_cnt}.png"
                shutil.copy(
                    os.path.join(dir1, filename), os.path.join(dir2, new_filename)
                )

                line_index = int(filename.split(".")[0]) - 1
                if 0 <= line_index < len(lines):
                    output_file.write(lines[line_index])


def clear_folder(folder_path):
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
            print(f"Failed to delete {file_path}. Reason: {e}")


def process_images(input_root, output_root):
    """
    input_root  = folder yang isinya img1/, img2/, dst.
                  di dalamnya ada split_img/ (berisi file png + position.txt)
    output_root = folder tujuan hasil pemrosesan
    """
    # clear_folder(output_root)
    os.makedirs(output_root, exist_ok=True)

    for img_name in os.listdir(input_root):
        img_dir = os.path.join(input_root, img_name, "split_img")
        if not os.path.isdir(img_dir):
            continue

        txt_file = os.path.join(img_dir, "position.txt")
        if not os.path.exists(txt_file):
            continue

        # folder tujuan -> ubah ke deduplicate_split_img
        dir2 = os.path.join(output_root, img_name, "deduplicate_split_img")
        output_txt_file = os.path.join(dir2, "position.txt")

        # bangun tree
        root_components, root_list = main(txt_file)
        for root_node in root_components:
            print_tree(root_node)
        print("Root list:", root_list)

        # copy hasil root saja
        copy_images_and_text(root_list, img_dir, dir2, txt_file, output_txt_file)


if __name__ == "__main__":
    input_root = "../results"  # folder berisi img1/, img2/, ...
    output_root = "../results"  # folder hasil keluaran
    process_images(input_root, output_root)
