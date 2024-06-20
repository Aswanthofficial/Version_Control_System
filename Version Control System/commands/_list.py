import os

def list():
    staging_area_dir = '.dvc/staging_area'
    for root, _, files in os.walk(staging_area_dir):
        for file in files:
                print(os.path.join(root, file).replace('\\', '/'))
