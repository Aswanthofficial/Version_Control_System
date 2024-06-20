def ignore(files_or_patterns):
    with open('.dvcignore', 'a') as f:
        for item in files_or_patterns:
            f.write(item + '\n')
    print("Files or patterns added to the ignore list.")
