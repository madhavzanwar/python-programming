a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

def greatest_num():
    if(a> b and a>c):
        print(f"{a} is greatest")
    elif(b>a and b>c):
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")        

greatest_num()