import os

def log():
    log_file = '.dvc/log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            print("Commit History:")
            for line in f:
                print(f"- {line.strip()}")
