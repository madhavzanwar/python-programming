#Write a Python program to print even and odd numbers from a user-defined range.
a = int(input("Enter starting value: "))
b = int(input("Enter ending value: "))
even = []
odd = []
print("Enter the first and last value of range", a, b)
for i in range(a, b+1):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers: ",even)
print("Odd numbers: ",odd)



