import shutil

def restore(backup_dir):
    shutil.rmtree('.dvc')
    shutil.copytree(backup_dir, '.dvc')
    print("Repository restored successfully.")
