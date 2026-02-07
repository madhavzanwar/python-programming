#FUNCTION JAB APNE AAP KO HI CALL KARTA HAI

# **Recursion** is when a function calls itself to solve a problem in smaller steps.

# It must have a **base case** to stop, or it will run forever.


def factorial(n):
    if(n == 0 or n== 1):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number: "))

print(f"The factorial of {n} is: {factorial(n)}")











    
