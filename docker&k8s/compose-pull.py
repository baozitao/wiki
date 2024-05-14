import subprocess
import yaml
from tabulate import tabulate
from tqdm import tqdm
import time

def get_images(compose_file):
    # 解析 docker-compose 文件获取所有服务的镜像
    with open(compose_file, "r") as f:
        compose_config = yaml.safe_load(f)
    images = []
    for service_name, service_config in compose_config.get("services", {}).items():
        image = service_config.get("image")
        if image:
            image_parts = image.split(":")
            if len(image_parts) == 2:
                images.append((service_name, image_parts[0], image_parts[1]))  # 拆分镜像名称和标签
            else:
                print(f"Image {image} format is incorrect, skipping...")
    return images

def prompt_pull(images):
    # 询问用户是否拉取镜像
    print("Here is the list of images to pull:")
    headers = ["No.", "Service Name", "Image", "Tag"]
    table_data = [[str(idx + 1), service_name, image, tag] for idx, (service_name, image, tag) in enumerate(images)]

    # 计算每列的最大宽度
    max_lengths = [max(len(row[i]) for row in table_data) for i in range(len(headers))]

    # 对齐表头
    headers_aligned = [header.ljust(max_length) for header, max_length in zip(headers, max_lengths)]

    # 对齐表格内容
    table_data_aligned = [[cell.ljust(max_length) for cell, max_length in zip(row, max_lengths)] for row in table_data]

    # 打印表格
    print(tabulate(table_data_aligned, headers=headers_aligned, tablefmt="grid", colalign=("center", "center", "center", "center")))
    choice = input("Do you want to pull these images? (y/yes/Enter to continue, anything else to cancel): ").strip().lower()
    return choice in ["y", "yes", ""]

def pull_arm64_images(images):
    # 拉取指定镜像的 ARM64 架构版本
    total_images = len(images)
    with tqdm(total=total_images, desc="Pulling Progress", unit="image", ncols=80, dynamic_ncols=True) as pbar:
        for service_name, image, tag in images:
            result = subprocess.run(["docker", "pull", "--platform", "arm64", f"{image}:{tag}"], capture_output=True, text=True)
            status = "Success" if result.returncode == 0 else "Failed"
            arch = "ARM64" if status == "Success" else "Unknown"
            pbar.set_postfix(Status=status, Architecture=arch)
            pbar.update(1)
            yield service_name, image, tag, status, arch

def export_images(images):
    choice = input("Do you want to export these images as a tar file? (y/yes/Enter to continue, anything else to cancel): ").strip().lower()
    if choice in ["y", "yes", ""]:
        with open("images.txt", "w") as f:
            for service_name, image, tag, status, arch in images:
                f.write(f"{image}:{tag} - {arch} Architecture - {'Pull Success' if status == 'Success' else 'Pull Failed'}\n")
        print("Exporting Progress:")
        subprocess.run(["tar", "-cvf", "images.tar", "images.txt"], stdout=subprocess.PIPE, text=True)

if __name__ == "__main__":
    compose_file = "docker-compose.yml"
    images = get_images(compose_file)
    if images:
        if prompt_pull(images):
            images = list(pull_arm64_images(images))
            print("Image pull completed!")
            export_images(images)
        else:
            print("Cancelled image pull.")
    else:
        print("No images to pull.")
