#Write a Python program to generate a list of random numbers and display the frequency of each number.
import random
from collections import Counter

# create empty list
numbers = []

# generate 20 random numbers
for i in range(20):
    num = random.randint(0, 100)
    numbers.append(num)

print("Random Numbers:", numbers)

# count frequency using Counter
freq = Counter(numbers)

print("\nFrequency of each number:")
for num, count in freq.items():
    print(num, ":", count) 