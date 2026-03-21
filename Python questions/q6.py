#Write a Python program to merge two dictionaries into one.
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = d1 | d2   # Python 3.9+

print(merged)