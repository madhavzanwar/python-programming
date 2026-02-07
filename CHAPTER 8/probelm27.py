#Write a recursive function to calculate the sum of first n natural numbers

n = int(input("Enter the number: "))

def sum(n):
    if(n==1): #base case
        return 1
    else:
        return sum(n-1) + n
    
print(sum(n))
    