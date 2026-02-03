# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user


a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))

total_percentage = (a + b + c) / 3

if (a < 33 or b < 33 or c < 33): ##a < 33 or b < 33 or c < 33  ✅a or b or c < 33❌##
    print("Student failed: individual subject criteria not met")

elif (total_percentage < 40):
    print("Student failed: overall percentage < 40")

else:
    print("Student passed: ",total_percentage)
