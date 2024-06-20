import os
import shutil

def commit(message):
    log_file = '.dvc/log'
    with open(log_file, 'a') as f:
        f.write(f"{message}\n")
    staging_area = '.dvc/staging_area'
    commits_dir = '.dvc/commits'
    if not os.path.exists(commits_dir):
        os.makedirs(commits_dir)
    for file in os.listdir(staging_area):
        shutil.copy(os.path.join(staging_area, file), os.path.join(commits_dir, file))
    print("Changes committed successfully.")
