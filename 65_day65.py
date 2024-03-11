# Day 65 of code!
# Write your code here.

# dict & help methods
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("Jhonny", 30)
print(p.__dict__)

print(help(Person))