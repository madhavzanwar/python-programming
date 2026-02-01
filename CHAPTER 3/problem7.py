#program to detect double space in string
#replace"  "by" "

string = input("Enter the string:")
print(string.find("  "))
print(string.replace("  "," "))

#if not present it will return -1
#strings are immutable function i.e. you cannot change them by doing any changes in them