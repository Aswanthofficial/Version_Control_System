import difflib

def diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.unified_diff(f1.readlines(), f2.readlines(), fromfile=file1, tofile=file2)
        print(''.join(diff))
