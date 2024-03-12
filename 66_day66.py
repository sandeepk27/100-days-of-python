# Day 66 of code!
# Write your code here.

# super keyword

class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
sandy = Programmer("Sandy", "2345", "Python")
print(sandy.name)
print(sandy.id)
print(sandy.lang)