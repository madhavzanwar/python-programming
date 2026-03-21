#Write a Python program to copy content from one file to another
with open("source.txt", "r") as f1:
    data = f1.read()

with open("destination.txt", "w") as f2:
    f2.write(data)

print("Content copied successfully")