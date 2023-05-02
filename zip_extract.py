import zipfile
import os
from pathlib import Path


def do_extract(filepaths, dest_dir):
    filepath = filepaths[0]
    filename = os.path.basename(filepath)
    files = filename.split('.')

    if files[1] == "zip":
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
        return True  # Extraction successful
    else:
        return False  # Extraction failed, not a zip file


if __name__ == "__main__":
    do_extract(filepaths=["/Users/amitabhishek/Desktop/xfiles.sh"],
               dest_dir="/Users/amitabhishek/Desktop/extract")
