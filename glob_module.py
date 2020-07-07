import os, glob

os.chdir("/Users/ianhill/Downloads")
for file in glob.glob("*.zip"):
    print(file)