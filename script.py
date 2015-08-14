import os
import shutil

# srcpath will be the location of the files you want to create a parent directory for based
# on the filnames within.

srcpath = "C:\\Users\\Your\\Location\\Goes\\Here\\Input"
srcfiles = os.listdir(srcpath)

# destpath will be the location where the newly created directory(s) will go

destpath = "C:\\Users\\Your\\Location\\Goes\\Here\\Output"

# extract the characters from the filenames and filter out duplicates
# the numbers 4 and 7 below will vary according to which characters within the filename you
# wish to carry to parent directory

destdirs = list(set([filename[4:7] for filename in srcfiles]))

def create(dirname, destpath):
    full_path = os.path.join(destpath, dirname)
    os.mkdir(full_path)
    return full_path

def move(filename, dirpath):
    shutil.move(os.path.join(srcpath, filename)
                ,dirpath)

# create destination directories and store their names along with full paths
targets = [
    (folder, create(folder, destpath)) for folder in destdirs
]

for dirname, full_path in targets:
    for filename in srcfiles:
        if dirname == filename[4:7]:
            move(filename, full_path)
