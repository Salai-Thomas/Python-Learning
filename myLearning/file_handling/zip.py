from zipfile import *

file = ZipFile("file.zip","w",ZIP_DEFLATED)
file.write("hello.txt")

file.close()