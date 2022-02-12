__author__ = 'tk'

# Start new file class9_type_casting_review
# VARIABLE TYPES AND TYPE CASTING REVIEW
#####################################################
# Reassigning Variables / Type Castings

int()  # full numbers
float()  # floating point numbers
str()  # strings
bool() # logical operators, data types

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



########################################################
# Task 4. We want to control float number decimals
# EXAMPLE 1
pi = 3.14159
print('Print %s' % 'Hello, World!')  # %s - string formatter
print('%f' % pi)  #  %f float formatter
print('%.2f' % pi)  # 2 decimal points - for display
print(round(pi))  # correct way to control decimal places for floats using math function round()


# EXAMPLE 2
given_float_number = 14.9873492873

# TREE METHODS TO CONTROL DECIMALS
print(round(given_float_number, 2)) # METHOD 1
print("{:.2f}".format(given_float_number)) # METHOD 2
print('Method ot print using %s  ' % '\'percentage sign s string formatter\'')
print('%f' % given_float_number) # METHOD 3 NO DECIMAL PLACES IDENTIFIER
print('%.2f' % given_float_number) # METHOD 3 WITH DECIMAL PLACES IDENTIFIER

# --------------- PYTHON OPERATORS --------------------

# start new file class9_operators

# Operators are used to perform operations on variables and values.

# Assignment / Reassignment
# Assignment Operator '='
# 1. Single Assignment
college = 'CCTB'
number_of_students = 30
duration_of_the_class = 45.0
in_session = True
print(f'College name: {college}')
print(f'Number of students: {number_of_students}')
print(f'Duration of the class: {duration_of_the_class}')
print(f'Class currently in session: {in_session}')

# 2. Multiple Assignment
# 2.1 Multiple Assignment one by one
season, month, year = 'Winter', 'January', 2022
print(season, month, year)

# 2.2 Chained Assignment
x = y = z = 20  # Hard Coded Values
print(x, y, z)

b = c = d = e = int(input('Enter year: '))  # Dynamic Values
print(b, c+1, d+2, e+3)

#####################################################
# BASIC MATH OPERATORS - ADDITIONS, SUBTRACTION, MULTIPLICATION, DIVISION

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

# Python Modulo Operator (Remainder)
# The modulus operator, sometimes also called the remainder operator (or integer remainder operator)
# works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second.
# In Python, the modulus operator is a percent sign ( % )
# How much will remain of the first number after the second number
# fits into it the maximum number of times
print(10 % 4)
print(15 % 12)
print(98 % 9)


# Do not divide by ZERO!
#print(100 / 0)

# How do the order of operations go in Python?
# P     Parenthesis,  then
# E     Exponents,  then
# MD    Multiplication and division, left to right, then
# AS    Addition and subtraction, left to right

# PEMDAS code
######################################################

#####################################################
# Data types / objects in Python

# create new file class9_list_set_tuple_dictionary

# Four collection data types: LIST, TUPLE, SET, DICTIONARY

######################################################
# 1. LIST
# LIST - List or Array is an object to store multiple values. Starts with zero (0)
# list is a collection that is ordered and changeable
# Lists are created with square brackets
list_of_something=[] # make a list with square brackets

list_of_names = ['John',  'Anna',  'James',  'Kim',  'Ben',  'Ray']
print(list_of_names)

# read value by calling a specific index, value 1 is read by calling index 0
print(list_of_names[0])

# update value in the list
list_of_names[3] = 'Jason'
print(list_of_names)

# append (add) new value to the list
list_of_names.append('Mike')
print(list_of_names)

# remove value the value using pop() command
list_of_names.pop(0)
print(list_of_names)

# clear
list_of_names.clear()
print(len(list_of_names))


# printing lists

tropical_list = ['Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee']

# Method 1: simple print()
print(tropical_list)

# Method 2: print using for loop, print every value on new line
for fruit in tropical_list:
    print(fruit)

# Using for loop + range print index : value pairs from a list or tuple
for i in range(len(tropical_list)):
    print(f'{i} : {tropical_list[i]}')

#####################################################
# 2. TUPLE
# Tuples are unchangeable, you cannot change,  add, remove items from the tuple.
# It's possible to convert tuple into a list, then make  changes and then convert it back tuple
# array of constants
# Tuple is a collection that is ordered and unchangeable.
# Allow duplicate members
# Tuples are used to store multiple items in a single variable
# Tuples are written with round () brackets


# create a tuple
print('------ tuple example ----------------')
yummy_tuple = ('apple', 'banana', 'mango', 'cherry', 'watermelon')
print(yummy_tuple)

# print items on new line using for loop
for yt in yummy_tuple:
    print(yt)

# print second item from the tuple (remember starts with zero)
print(yummy_tuple[1])

# update tuple
yummy_list = list(yummy_tuple) # to change a tuple, cast it into list using list() function

# append and item
yummy_list.append('nectarine')
print(yummy_list)

# remove an item
yummy_list.pop(4)
print(yummy_list)

# convert back to tuple
yummy_tuple = tuple(yummy_list)
print(yummy_tuple)
print('------ end tuple example ----------------')

#####################################################
# 3. SET
# Set is unhonored, unchangeable (unmutable) and unindexed. No duplicate memebers are allowed
# Sets are written in curly braces
print('------ set example ----------------')
yummy_set = {'apple', 'banana', 'mango', 'cherry', 'watermelon'}
print(yummy_set)

for ys in yummy_set:
    print(ys)
print('------ end set example ----------------')
#####################################################
# 4. DICTIONARY
# Dictionary is a key:value pair collection which is ordered, changeable, no duplicate members
#
student = {
    'name': 'John Smith',
    'cohort': '2',
    'year': '2021',
    'grade': 100
}

new_user = {
    'username': 'testuser99',
    'password': 'Pass1',
    'firstname': 'Test',
    'lastname': 'User',
    'email': 'testuser99@gmail.com'
}

# Display all
print(student)
print(new_user)

# keys only
print(student.keys())
print(new_user.keys())

# keys and values as dict_items container
print(student.items())
print(new_user.items())

# values only
print(student.values())
print(new_user.values())

# Display values for the key
print(student.get('brand'))
print(new_user.get("password"))

# Change the value of key
#method 1
student.update({'cohort': '3'})
new_user.update({'password': 'Pswd3!'})

print(student)
print(new_user)

# Method 2
# update value for a specified key
student['year'] = '2022'
new_user['username'] = 'happyuser'

print(student)
print(new_user)

# ###########LIST VS SET VS TUPLE VS DICTIONARY PRACTICE ################
a = [1, 2, 3, 'a', 1, 3, 5] # create list
print(a)
print(tuple(a))
print(set(a)) # unique values only

b = {'a', 1, 4, 8} # create set
print(b)
print(list(b))
print(tuple(b))

# Make Dictionary from 2 lists
key_lst= ['username', 'password', 'firstname','lastname', 'email']
val_lst = ['testuser99', 'Pass1', 'Test','User', 'testuser99@google.com']

dic_lst = {key_lst[i]: val_lst[i] for i in range(len(key_lst))}
print(dic_lst)