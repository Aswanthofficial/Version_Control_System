import os

def annotate(file_path):
    dvc_file = file_path + '.dvc'
    if os.path.exists(dvc_file):
        with open(dvc_file, 'r') as f:
            print(f"Annotations for '{file_path}':")
            print(f.read())
    else:
        print(f"Error: DVC file '{dvc_file}' does not exist.")
