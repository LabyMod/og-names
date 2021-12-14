import os

for subdir, dirs, files in os.walk("src"):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".txt"):
            with open(filepath, 'r') as read:
                names = sorted(set(read.readlines()))
            with open(filepath, 'w') as write:
                write.writelines(names)
