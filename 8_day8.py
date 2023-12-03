# Strings in python
name = "Sandeep"
friend = "Albert"
anotherFriend = 'Lovish'
greet = '''He said, 
Hi Sid
hey I am good
"What about you'''

print("Hello, " + name)
# print(apple) 
print(name[0]+name[1]+name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

# print(name[]) # Throws an error
print("Lets use a for loop\n")
for character in greet:
    print(character)
