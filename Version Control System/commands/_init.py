import os

def init():
    if not os.path.exists('.dvc'):
        os.makedirs('.dvc')
    if not os.path.exists('.dvc/cache'):
        os.makedirs('.dvc/cache')
    if not os.path.exists('.dvc/snapshots'):
        os.makedirs('.dvc/snapshots')
    if not os.path.exists('.dvc/staging_area'):
        os.makedirs('.dvc/staging_area')
    if not os.path.exists('.dvc/log'):
        with open('.dvc/log', 'w') as f:
            f.write("DVC log file\n")
    if not os.path.exists('.dvc/commits'):
        os.makedirs('.dvc/commits')
    print("DVC initialized successfully.")
