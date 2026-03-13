# Multilevel Inheritance Example

class Animal:          # Grandparent class
    def eat(self):
        print("Animal eats food")

class Dog(Animal):     # Parent class (inherits Animal)
    def bark(self):
        print("Dog barks")

class Puppy(Dog):      # Child class (inherits Dog)
    def weep(self):
        print("Puppy weeps")


# Creating object of the lowest class
p = Puppy()

# Accessing methods from all levels
p.eat()     # from Animal
p.bark()    # from Dog
p.weep()    # from Puppy