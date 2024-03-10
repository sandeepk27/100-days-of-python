# Day 60 of code!
# Write your code here.

# static methods
class Math:
  def __init__(self, num):
    self.num = num

  def addnum(self, n):
    self.num = self.num +n
    
  @staticmethod
  def add(a, b):
      return a + b

# result = Math.add(1, 2)
# print(result) # Output: 3
a = Math(5)
print(a.num)
a.addnum(6)
print(a.num)

print(Math.add(7, 2)) 