import zipfile

# Zipping files
with zipfile.ZipFile("myarchive.zip", "w") as z:
    z.write("file1.txt")
    z.write("file2.txt")
print("Files zipped successfully!")

# Unzipping files
with zipfile.ZipFile("myarchive.zip", "r") as z:
    z.extractall("unzipped_files")
print("Files unzipped successfully!")
