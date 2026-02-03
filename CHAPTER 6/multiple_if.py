a  = int(input("Enter a number:"))

if(a%2 == 0):
    print("Number is even")

#end of first if statement

if(a%5 == 0):
    print("number is divisible by 5")
else:
    print("Number is not divisible by 5")

#end of second if statement

#BOTH IFs STATEMENTS ARE INDEPENDENT OF EACH OTHER
#else and elif cant be present only whereas if can be
#last else is only executed when all elif fail
