# Day 50 of code!
# Write your code here.

# map and filter functions

# # MAP 
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # li = []
# # for item in l:
# #   li.append(cube(item))

# li = list(map(lambda x: x*x*x, l))
# print(li)

# # FILTER
# def filter_function(a):
#   return a>2
  
# list = list(filter(filter_function, l))
# print(list)

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5] 

# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
  return x + y
  
sum = reduce(mysum, numbers)

# Print the sum
print(sum)