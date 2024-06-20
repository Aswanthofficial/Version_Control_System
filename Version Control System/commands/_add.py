import os
import hashlib
import shutil

def add(file_path):
    file_path = str(file_path)
    if os.path.exists(file_path):
        staging_path = os.path.join('.dvc', 'staging_area', os.path.basename(file_path))
        shutil.copyfile(file_path, staging_path)

        checksum = None
        with open(staging_path, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()        

        dvc_file = file_path + '.dvc'
        with open(dvc_file, 'w') as f:
            f.write(f'checksum: {checksum}\n')
            f.write(f'path: {staging_path}\n')        

        print(f"Added '{file_path}' to DVC staging area.")
    else:
        print(f"Error: File '{file_path}' does not exist.")
