# **Built-in functions** are pre-made functions provided by Python (like `print()`, `len()`, `max()`).

# **User-defined functions** are functions you create using `def` to perform your own tasks.


# Built-in Functions Examples

numbers = [5, 2, 9, 1]

print("Length:", len(numbers))     # len()
print("Maximum:", max(numbers))    # max()
print("Minimum:", min(numbers))    # min()
print("Sum:", sum(numbers))        # sum()

name = "Madhav"
print("Uppercase:", name.upper())  # built-in string method



# User-defined Functions


# Function to greet user
def greet(name):
    return f"Hello, {name}! Welcome to Python."

# Function to add two numbers
def add(a, b):
    return a + b

# Function to check even/odd
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"



# Function Calls


print(greet("Madhav"))
print("Addition:", add(10, 5))
print("Number is:", check_even(7))

