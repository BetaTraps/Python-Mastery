# integer (wholenumbers)
import math
students_count = 1000
# float (decimals)
rating = 3.99
# boolean (true/false)
is_published = False
# string (Text)
course_name = "Python Programing"

# Nameing convention in python uses
# lower case such as 'rating' above
# if multi word variables use a '_'
# such as "course_name"

# String's
print("\nStrings's\n")
course = "Python Programming"
message = """
this is how you can do strings with multi

lines
blah blah blah
"""
# This gets the length of strings
print(len(course))
# Get a certain char in a string (0 gets the first charagter
# -1 gets the laste character in the string)
print(course[0])
print(course[-1])
# This is how you get a sub partion of a string (if done include
# the end index will return everything from the first index to the end and vesversa )
print(course[0:3])
print(course[3:])
print(course[:3])
print(course[:])

# Escape Sequences example : the '\' is a escape character in a string to
# get a "" or '' when needed in a string
# \" : "
# \' : '
# \\ : \
# \n : new Line
print("\nEscape Sequences\n")
course_string = "Python \"Programming\""
print(course_string)

# Formatted Strings : putting a f"" allows for string interperlation
# and in the { } add the variable into the string
print("\nFormatted Strings\n")
first = "David"
last = "Pilot"
full = first + " " + last
print(full)
full_name = f"{first} {last}"
print(full_name)

# String Methods
# string .upper() sets the text to uppercase
# .lower() set the text to lowecase
# .title() set a string "pi pi" to "Pi Pi"
# .strip() removes whitespace at the beginning then there is .lstrip() for left and .rstrip() for right
# .find("")  finds the index of the char or string in find on the original string if not found returns -1
# .replace("p", "j") replaces first char with other char in orignal string
# ("" in string) returns a true or false if the chars you are searching for in string is found or not
# ("" not in string) returns true or false if chars not in the string
print("\nString Methods\n")
test_methods = "  python programming"
print(test_methods.upper())
print(test_methods.lower())
print(test_methods.title())
print(test_methods.strip())
print(test_methods.find("pro"))
print(test_methods.replace("p", "j"))
print("pro" in test_methods)
print("swift" not in test_methods)

# Numbers
print("\nNumbers\n")
x = 1
x = 1.1
x = 1+2j  # a + bi   j : is i for complex numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # remove remander
print(10 % 3)  # remander of a division
print(10 ** 3)  # 10^3

x = 10
x = x + 3
x += 3

# Working with Numbers
print("\nWorking with Numbers\n")


print(round(2.9))  # rounds the number
print(abs(-2.9))  # absolute value
print(math.ceil(2.2))  # rounds up
# Python3 math module https://docs.python.org/3/library/math.html

# Type Conversion
# int(x)
# float(x)
# bool(x) false : (0, "", None)  true: anything with a value
# str(x)
# type(x) returns the current type of variable
print("\nType COnversion\n")
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
