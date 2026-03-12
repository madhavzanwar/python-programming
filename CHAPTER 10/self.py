#self refers to the instance of the class. It is automatically passed with a function call
#from an object.

class okay:
    company = "Goggle"
    def getSalary(self):
        print("Salary is not there")

#static method - 
#Sometimes we need a function that does not use the self-parameter. We can define a
#static method like this:
@staticmethod # decorator to mark greet as a static method
def greet():
    print("Hello user")


#__INIT__() CONSTRUCTOR
#__init__() is a special method which is first run as soon as the object is created.
#__init__() method is also known as constructor.
#It takes ‘self’ argument and can also take further arguments.