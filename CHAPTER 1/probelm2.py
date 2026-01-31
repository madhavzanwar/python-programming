#program to print contents of a directory using os module

import os

directory_path = '/'

contents = os.listdir(directory_path)

for item in contents:
    print(item)