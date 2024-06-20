import os
import shutil
from datetime import datetime

def snapshot(snapshot_name):
    snapshot_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_dir = f'.dvc/snapshots/{snapshot_time}_{snapshot_name}'
    shutil.copytree('.dvc', snapshot_dir)
    print(f"Snapshot '{snapshot_name}' created successfully.")
