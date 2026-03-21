#Write a Python program to check whether a number is prime or not.
a = int(input("Enter number: "))

if a <= 1:
    print("Not prime")
else:
    for i in range(2, a):
        if a % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")