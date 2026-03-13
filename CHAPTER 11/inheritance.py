# Demonstration of Inheritance in Python

class Employee:
    company = "ITC"   # Class attribute (shared by all Employee objects)

    def show(self):
        # self refers to the current object
        # instance attributes like name and salary must exist before using
        print(f"The name of employee is {self.name} and the salary is {self.salary}")


# Child class inheriting from Employee
class Programmer(Employee):
    company = "ITC Infotech"   # Overrides parent class attribute

    def show(self):
        # Method overriding (same method name as parent)
        print(f"The name of employee is {self.name} and the salary is {self.salary}")


# Creating objects
a = Employee()
b = Programmer()

# Accessing class attributes
print(a.company, b.company)

