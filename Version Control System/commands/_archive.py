import shutil

def archive(archive_name):
    shutil.make_archive(archive_name, 'zip', '.dvc')
    print("Repository archived successfully.")
