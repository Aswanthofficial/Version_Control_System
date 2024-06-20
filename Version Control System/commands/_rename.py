import os

def rename(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"Renamed '{old_name}' to '{new_name}'.")
