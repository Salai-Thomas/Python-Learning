import os

file_name = "hello1.txt"
if os.path.isfile(file_name):
    print("File Exist")
else:
    print("File Does Not Exist")