# CLASS in Python

class Employee:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
    
    def fullName(self):
        print("Full Name is : " + self.firstName + " " + self.lastName)


emp1_obj = Employee("Peter", "Paul", 33) 
emp2_obj = Employee("Tina", "Joseph", 30) 

print(f"Age of Employee 1 : {emp1_obj.age}")
emp1_obj.fullName()

print(f"Age of Employee 2 : {emp2_obj.age}")
emp2_obj.fullName()






