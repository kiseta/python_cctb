__author__ = 'tk'
# INPUT VALUES FROM THE USER IN PYTHON

# hardcoded values
name = 'Edward'
print("Hello,", name)
activity = 'playing piano'
print('You are very good at', activity)
birth_year = 1901
print('You are now', 2022 - birth_year, 'years old')

# use input() function to prompt the user to input values
name = input('What is your name?: ')
print(f'Hello, {name}!')
activity = input('What are you doing?: ')
print(f'You are very good at {activity}')
birth_year = int(input('What year you were born?: '))
age = 2022 - birth_year
print(f'You are now {age} years old')


# combine print and input command
print('Hello,', input('Please enter your name: '))

# Multipe inputs in one go
a, b, c = input('Enter three values separated by space: ').split()
input().split()
print(a, b, c)

# reverse string
movie = input('Enter your favorite movie title: ')
print('Reverse is: ', movie[::-1].lower())

# variable naming conventions

# incorrect variable names
# cannot start variable with the number
# 77varname - incorrect

# no special characters in variable name, anything on the keyboard Shift+1-0 '_' is ok
# first_name = 'john'
# last_name = 'smith'

# non-latin alphabet charters, some will work but not everywhere and not a common practice
# Ð°Ð´Ñ€ÐµÑ = '123 Main st'

# best variable naming conventions - lower case, then numbers, then underscores
var_name = 10
var10 = 10
var_10 = 10

# UPPER CASE LETTER USED FOR CONSTANTS
NUMBER_OF_DAYS_IN_A_YEAR = 365
NUMBER_OF_HOURS_IN_A_DAY = 24

print(f'Number of hours in a day on Earth: {NUMBER_OF_HOURS_IN_A_DAY}')
print(f'Unless you are on Marse then it\'s {NUMBER_OF_HOURS_IN_A_DAY +1}')

# variable are assigned from left to right
# variable_name = variable value - correct assignment
# variable value = variable name - incorrect

# Variable names cannot be used if they are already reserved in Python - Python reserved words
# int, str, bool, float, for, while, break, continue, try, except, finally, True, False, input, split,
# if, else, elif, and, or
# Python built-in function - can not be used as variable names
# Python built-in functions list: https://docs.python.org/3/library/functions.html

# multiple variable assignments
# in place swapping of two number
x, y = 10, 20
print(x, y)
x, y = y, x
print(x, y)

# Print a string n times
n = 3
s = 'Let it snow!'
p = " "  # blank spae
print((s + p) * 3)

# Multiple input values in a single line
# name, color, quantity = input('Enter ingredient name, color and quantity separated by space: ').split()
# print(f'Ingredient Name: {name}')
# print(f'Ingredient Color: {color}')
# print(f'Ingredient Quantity: {quantity}')

# check memory usage of the variable
import sys

m = "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only " \
    "Mercury. In English, Mars carries the name of the Roman god of war and is often referred to as the \'Red Planet\'"

print(m)
print(f'Memory Usage in bytes: {sys.getsizeof(m)}')

# spliting a string into a list (lists in Python are multi-value variable type and we will talk about them im more details later)
conf_msg = 'Thank you for your order. Your tracking number is TR203948023948'
print(conf_msg)
conf_msg_split = conf_msg.split()
print(conf_msg_split)
print(len(conf_msg_split)) # print the length of the list - zero based, first item is index 0
tracking_num = conf_msg_split[-1]
print(f'Your tracking number is: {tracking_num}') # capture last item