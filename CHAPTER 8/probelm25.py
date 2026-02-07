#convert celsuis to farenheit

temp = int(input("Enter the temp in celsius: "))

def cel_to_f():
    f = (temp * 1.8) + 32
    print(f"The temp in farenheit is: {f}")

cel_to_f()