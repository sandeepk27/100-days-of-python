# Day 44 of code!
# Write your code here.x = 10  # global variable

# local vs global variables
def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # It prints 5
#print(y) # this will cause an error because y is a local variable and is not accessible outside of the function