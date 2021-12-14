import os
import re

# Script to sort all names, remove duplicated names and match the Minecraft username regex pattern

for subdir, dirs, files in os.walk("src"):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".txt"):
            with open(filepath, 'r') as read:
                names = sorted(set(read.readlines()))
                names = [name for name in names if re.match(r"^[A-Za-z0-9_]{2,16}$", name.rstrip())]
            with open(filepath, 'w') as write:
                write.writelines(names)