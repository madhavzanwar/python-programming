#Write a Python program to reverse a tuple and access specific elements from it.
t = (1, 2, 3, 4, 5)

# reverse tuple
rev = t[::-1]

print("Original:", t)
print("Reversed:", rev)

# access elements
print("First element:", t[0])
print("Last element:", t[-1])