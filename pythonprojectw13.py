import os

files = []

for file_name in os.listdir(os.getcwd()):
    file_info = {
        "name": file_name,
        "size": os.path.getsize(file_name),
    }
    files.append(file_info)
    
for file in files:
    print("Name:", file["name"])
    print("Size", file["size"], "bytes")
    print("")