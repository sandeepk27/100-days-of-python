# Strings are immutable
a = "!!!Sandy!! !!!! Sandeep"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Sandy", "Shiv"))
print(a.split(" "))
blogHeading = "strings in python"
print(blogHeading.capitalize())
print(blogHeading.lower())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Sandeep"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
print(str1.index("s"))
print(str1.count('H'))

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())
# str1 = "Welcome"
# print(str1.isalpha())

# str1 = "hello world"
# print(str1.islower())

# str1 = "We wish you a Merry Christmas\n"
# print(str1.isprintable())
# str1 = "         "       #using Spacebar
# print(str1.isspace())
# str2 = "  "       #using Tab
# print(str2.isspace())

# str1 = "World Health Organization" 
# print(str1.istitle())

# str2 = "To kill a Mocking bird"
# print(str2.istitle())

# str1 = "Python is a Interpreted Language" 
# print(str1.startswith("Python"))

# str1 = "Python is a Interpreted Language" 
# print(str1.swapcase())

# str1 = "His name is Dan. Dan is an honest man."
# print(str1.title())