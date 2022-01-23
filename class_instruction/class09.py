__author__ = 'tk'
# Combine print and input commands together
print('Hello, ', input('Enter your name: '))

# Multiple Inputs in one go
a, b, c, d, e, f = input('Enter three inputs with space and without commas: ').split()
print(a, b, c, d, e, f)

# Reversing a string
name = input('Enter your name: ')
print("Reverse is", name[::-1])

# In-place swapping of two numbers
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# Check the memory usage of an object
import sys
x = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s ' \
    'standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make ' \
    'a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, ' \
    'remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing '
y = ((4*4)*(77777777*7667676767676))*2
print(sys.getsizeof(y))

# Print string N times
n = 2
a = "Python is the best. I'm gonna say this twice"
s = " "
print((a+s) * n)

# Splitting a string into a list
x = 'Python is a great language to start'
y = x.split()
print(y)

# Multiple input values in a single line
name, age, city = input('Enter your info separated by space: ').split()
print('Student name:', name)
print('Student age:', age)
print('Student city:', city)

# Define a simple variables
first_name = 'Alexander'  # STATIC OR HARD CODED VALUE
last_name = 'Shevchenko'  # STATIC OR HARD CODED VALUE
print(first_name)
print(last_name)

# Define a simple variables
first_name = input('Enter your first name: ')  # DYNAMIC VALUE
last_name = input('Enter your last name: ')  # DYNAMIC VALUE
print(first_name)
print(last_name)

# MISTAKES IN A VARIABLE NAMES
# 1. We can't start a variable name with number
# 1movie = 'Mask'
#print(1movie)

# 2. We can't use spacial characters in the variable name
# WHEN YOU PRESS SHIFT AND 1, 2, 3...0
#var_x! = 10
#print(var_x!)

# 3. Avoid using non-Latin alphabet (Chinese, Arabic, Hebrew, Russian etc)
# Ð¿Ñ€Ð¸Ð²Ñ–Ñ‚ = 10
# print(Ð¿Ñ€Ð¸Ð²Ñ–Ñ‚)

# NAMING RULES.
#1. First letter, then numbers or underscores
var_number = 10
var10 = 10
var_10 = 10

# Constant variables - upper case letter in the var name
STUDENTS = 30
print(STUDENTS)

# Python is case-sensitive programming language
# lower
minecraft_items = '5 5 5'
print(minecraft_items)
# title
Minecraft_Items = '5 5 5' * 2
print(Minecraft_Items)
# upper
MINECRAFT_ITEMS = '5 5 5'
print(MINECRAFT_ITEMS)

# Variables must be assigned from left to right.
# "Hello, world" = greeting

# Variable names cannot be used if they already reserved by Python.
# int, str, bool, float, for, while, break, continue, try, except, finally, True, False, if, elif, else, and, or
# Variable names cannot be used as Python built-in functions
# https://docs.python.org/3/library/functions.html
