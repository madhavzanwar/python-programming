a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

if(a>=b and a>=c and a>=d):
    print("First number is largest")

elif(b>=a and b>=c and b>=d):
    print("Second number is largest")

elif(c>=a and c>=b and c>=d):
    print("Third number is largest")

else:
    print("Fourth number is largest")
