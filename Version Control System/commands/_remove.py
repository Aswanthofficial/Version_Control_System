import os

def remove(files):
    for dvc_file in files:        
        if os.path.exists(f'.dvc/staging_area/{dvc_file}'):
            os.remove(f'.dvc/staging_area/{dvc_file}')
            print(f"Removed '{dvc_file}' from the DVC staging area.")
        else:
            print(f"File '{dvc_file}' is not staged.")