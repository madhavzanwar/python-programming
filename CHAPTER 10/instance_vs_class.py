#An attribute that belongs to the Instance (object)
#Instance attributes, take preference over class attributes during assignment &
#retrieval.

class Employee:
    name = "Madhav"
    age = "19"
    salary = 5000000

yo = Employee()
yo.age = "20"    #19 print nhi hoga coz of priority
print(yo.name, yo.age)