__author__ = 'tk'
# Reassigning Variable/ Type Casting
int()
float()
str()
bool()

# Task 1. Convert data types into integers
a = int(1)
b = int(9.67) # convert float to int
c = int('2002')
print(a, b, c*2,'\n')

# Task 2. Convert data types into float numbers

d = float(1) # int into float
e = float(9.67) # float into float
f = float('2002')
g = float('2002.90')
print(d, e, f, g)

# Task 3. Convert data types into strings

h = str('gh23')
i = str(89*2)
j = str(56.0*2)
k = str(True*2)
print(h, i, j, k)

# Task 4. Control float number decimals

pi = 3.1415926535
rnd_pi = round(pi, 2)
f1_pi = '%.2f' % pi
f2_pi= "{:.2f}".format(pi)
print(rnd_pi)
print(f1_pi)
print(f2_pi)

print('%s' % 'Hello, World!')
print('%.2f' % pi)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Assignment / Reassignment
# Assignment operator= 0
# 1. Single Assignment
college = 'CCTB'
number_of_students = 30
class_duration = 45.0
print(f'College name: {college}')
print(f'Number of Students: {number_of_students}')
print(f'Duration of the Class: {class_duration}')

# 2. Multiple Assignments
# 2.1 One by one
season, month, year = 'Winter','January',2022
print(season, month, year)

# 2.2 Chained Assignment
x = y = z = 20 # hardcoded value assignment
print(x, y, z)

# b = c = d = e = int(input('Enter year: ')) # Dynamic Values
# print(b, c, d, e)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Basic Operators
# Depending on datatype, Python allows arithmetic operations
# INT = all operators(*, /, -, +)
# FLOAT = all operators(*, /, -, +)
# STR = only addition or multiplication
# FLOAT = all operators(*, /, -, +), True = 1, False = 0
print(True * 2)
print(False * 2)

# Basic Operators. Multiplication
# * single muliplication
print(8 * 65)

# ** - exponent, power multiplication
print(2 ** 5) # 2 * 2 * 2 * 2 * 2= 32

# Basic Operators. Divisions
# regular divisions - one forward slash / in one line
print(100 / 2)

# integer divison -  two forward slashed
print(100 // 2)

# Python Modulo Operator
print(10 % 4)
#print(100 / 0) # can't divide by zero

print('Click \'Submit\' button')

# How to do the order of operations in Python - PEMDAS code
# P Parenthesis, then
# E Exponents, then
# MD Multiplications and divisions,  left to right
# AS Additions and Substactions, left to right


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Data types / objects in Python
list_of_names = ['Jack',  'Sparrow',  'Nina',  'Bruce',  'Justin',  'Tatyana']
# LIST - List or Array is an object to store multiple values. Starts with zero (0)
# list is a collection that is ordered and changeable

print(list_of_names)

# read values by calling a specific index
print(list_of_names[0])

# update value in the list
list_of_names[0] = 'George'
print(list_of_names)

# append
list_of_names.append('Nona')
print(list_of_names)

# remove value
list_of_names.pop(0)
print(list_of_names)

# clear
#list_of_names.clear()
print(len(list_of_names))
