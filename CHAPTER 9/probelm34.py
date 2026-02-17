'''Write a program to find out whether a file is identical & matches the content of
another file.
'''

with open("CHAPTER 9/file1.txt", "r") as f1:
    content1 = f1.read()

with open("CHAPTER 9/file2.txt", "r") as f2:
    content2 = f2.read()

if content1 == content2:
    print("Both files are identical ")
else:
    print("Files are different ")
