# Day 53 of code!
# Write your code here.

# class and objects

class Person:
  name = "Sandeep"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Sarthak"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
