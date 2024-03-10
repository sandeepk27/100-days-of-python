# Day 48 of code!
# Write your code here.

# seek and tell functions

with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(3)

with open('sample.txt', 'r') as f:
  print(f.read())