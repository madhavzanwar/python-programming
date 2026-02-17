#Write a program to read the text from a given file ‘poems.txt’ and find out
#whether it contains the word ‘twinkle’.

with open("CHAPTER 9/poems.txt") as f:
    data = f.read()
 


if("twinkle" in data):
    print("twinkle is present in data")

else:
    print("Twinkle is not present in content")