import os

def list_files(startpath):
    filenames = []

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            filenames.append(startpath + "/" + f)

    return filenames

def list_filenames(startpath):
    filenames = []

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            filenames.append(f)

    return filenames


