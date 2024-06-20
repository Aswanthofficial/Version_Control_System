import shutil

def patch(patch_file, target_dir):
    shutil.unpack_archive(patch_file, target_dir)
    print(f"Patched '{target_dir}' successfully.")
