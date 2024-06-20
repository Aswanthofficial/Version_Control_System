import os

def clean():
    for root, _, files in os.walk('.dvc/cache'):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
            print(f"Removed cache file: {file_path}")
    print("Cache cleaned successfully.")
