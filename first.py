import os
import shutil
from concurrent.futures import ThreadPoolExecutor
import sys

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def copy_file(file_path, target_directory):
    file_extension = file_path.split('.')[-1]
    target_dir = os.path.join(target_directory, file_extension)
    create_directory(target_dir)
    shutil.copy2(file_path, target_dir)

def process_directory(source_directory, target_directory):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(copy_file, file_path, target_directory)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<target_directory>]")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    create_directory(target_directory)
    process_directory(source_directory, target_directory)
