f = open("CHAPTER 9/file.txt")


lines = f.readlines()

print(lines, type(lines))


f.close()


#modes of opening a file: 
'''
r - open for reading
w - open for writing
a - open for appending
+ - open for updating.
rb will open for read in binary mode.
rt will open for read in text mode.
'''

with open("Myfile.txt") as f:
    print(f.read())

#you don't have to explicitly close the file after this    