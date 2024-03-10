# Day 57 of code!
# Write your code here.

# Inheritance in python

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id 

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLanguage(self):
    print("The default language is Python")


e1 = Employee("Krish Das", 400)
e1.showDetails()
e2 = Programmer("Sandeep", 4100)
e2.showDetails()
e2.showLanguage() 