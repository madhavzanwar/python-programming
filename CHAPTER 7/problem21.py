#star pattern
'''
for n = 3:
  *
 ***
*****

'''

n = int(input("Enter the value of n: "))

for i in range(1, n+1):
    print(" "* (n-i), end=" ")
    print("*"*(2*i - 1), end=" ")
    print(" ")


#spaces decrease
#stars increase
'''
end="" → stay on same line
end=" " → add space then stay
end="\n" → default (next line)
'''