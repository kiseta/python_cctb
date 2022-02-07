__author__ = 'tk'
#####################################################
# Reassigning Variables / Type Castings
int()
float()
str()
bool()

# Task 1. Convert data types into integers
a = int(1)
b = int(9.67)  # convert float into int
c = int('2022')  # convert str into int
print(a, b, c * 2)

# Task 2. Convert data types into float numbers
d = float(1)  # convert int into float
e = float(9.67)  # convert float into float
f = float('2022')  # convert str into float
g = float('2022.99')  # convert str into float
print(d, e, f, g)

# Task 3. Convert data types into strings
h = str('gh23')
i = str(89)
j = str(56.0 * 2)
k = str(True * 2)
print(h, i * 2, j, k)

# Task 4. We want to control float number decimals
given_float_number = 14.2222222222
updated_float_number = round(given_float_number, 2)
print(updated_float_number)

print("{:.2f}".format(given_float_number))

#####################################################

# Assignment / Reassignment
# Assignment Operator =
# 1. Single Assignment
college = 'CCTB'
number_of_students = 30
duration_of_the_class = 45.0
print(f'College name: {college}')
print(f'Number of students: {number_of_students}')
print(f'Duration of the class: {duration_of_the_class}')

# 2. Multiple Assignment
# 2.1 Multiple Assignment one by one
season, month, year = 'Winter', 'January', 2022
print(season, month, year)

# 2.2 Chained Assignment
x = y = z = 20  # Hard Coded Values
print(x, y, z)

# b = c = d = e = int(input('Enter year: '))  # Dynamic Values
# print(b, c, d, e)

#####################################################
# Basic Operators
# Depends on data type, Python allows arithmetic operations
# INT = all operators(*, /, -, +)
# FLOAT = all operators(*, /, -, +)
# STR = only addition or multiplication
# BOOL = all operators(*, /, -, +), but True is always 1, and False is 0 (binary value)
print(True * 2)  # --> 2, because True is 1
print(False * 2)  # --> 0, because False is 0

# Basic Operators. Multiplication
# * - single multiplication
print(8 * 20)

# ** - power multiplication
print(2 ** 5)  # 2 * 2 * 2 * 2 * 2 = 32

# Basic Operators. Division
# regular division - one forward slash in one line
print(100 / 2)  # 50.0

# integer division - two forward slashes in one line
print(100 // 2)  # 50

# Python Modulo Operator
# How much will remain of the first number after the second number
# fits into it the maximum number of times
print(10 % 4)

# Do not divide by ZERO!
#print(100 / 0)

# How do the order of operations go in Python?
# P     Parenthesis,  then
# E     Exponents,  then
# MD    Multiplication and division, left to right, then
# AS    Addition and subtraction, left to right

# PEMDAS code

#####################################################
# Data types / objects in Python
# LIST - List or Array is an object to store multiple values and manipulate with them
# by indexes.
list_of_names = ['Jack', 'Sparrow', 'Nina', 'Bruce', 'Justin', 'Tatyana']
# Indexes are numbers or ID's of values. Always starting with 0.
# List is o collection which is ordered and changeable. Allow duplicated items.
print(list_of_names)

# We can read values by calling the indexes (always start with 0)
print(list_of_names[0])

# We can update values by calling the indexes (always start with 0)
list_of_names[0] = 'George'
print(list_of_names[0])

# We can add (append) value to the end of the list
list_of_names.append('Nona')
print(list_of_names[-1])

# We can remove value from the list
list_of_names.pop(0)
print(list_of_names)

# We can clear the list at all
list_of_names.clear()
print(list_of_names)

# We can check length of the list
list_of_names = ['Jack', 'Sparrow', 'Nina', 'Bruce', 'Justin', 'Tatyana']
print(len(list_of_names))