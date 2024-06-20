import os
import shutil
import hashlib

def revert(file_path, version):
    dvc_file = file_path + '.dvc'
    if os.path.exists(dvc_file):
        with open(dvc_file, 'r') as f:
            metadata = f.readlines()        
        original_file_path = metadata[1].split(': ')[1].strip()
        original_checksum = metadata[0].split(': ')[1].strip()        
        with open(original_file_path, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()        
        if checksum == original_checksum:
            print(f"Data file '{file_path}' is already at its original state. No action taken.")
            return
        version_cache_dir = os.path.join('.dvc', 'cache', version[:2], version[2:])
        version_cache_file = os.path.join(version_cache_dir, original_checksum)
        if os.path.exists(version_cache_file):
            shutil.copy(version_cache_file, original_file_path)
            print(f"Successfully reverted '{file_path}' to version '{version}'.")
        else:
            print(f"Error: Version '{version}' cache file '{version_cache_file}' not found.")
    else:
        print(f"Error: DVC file '{dvc_file}' does not exist.")
