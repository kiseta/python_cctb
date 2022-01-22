__author__ = 'tk'
# Tatyana
# Lab Assignment 10 - Loops
# Create a new Python file with the name 'lab10{your_name}.py' and Save it.
# Do the following tasks.

# 1. Print individual letters of a string using the FOR LOOP. Enter value using input () command.
anyword = input('Enter any word: ')
for l in anyword:
    print(l)

# 2. Make a program using FOR LOOP to iterate over a Python list or tuple. The list should have at least 5 elements.

favorite_fruit = ['Nectarine', 'Mango', 'Durian', 'Canistel', 'Cherimoya']
for fruit in favorite_fruit:
    print(f'I love {fruit}!')

# 3. Make a program using FOR LOOP to find the sum of all integer numbers stored in a list.
int_list = [121, 45, 7, 13, 27, 43, 89, 1515, 999]

# create a variable to store the total
total = 0

# iterate over the list of numbers
print('Add the following Numbers:')
for i in int_list:
    print(i, '+')
    total = total + i
print('-----------------------')
print(f'Total: {total}')

# 4. Make a program using WHILE LOOP to start at 1 and stop at 1000.
n = 1
while n < 1000:  # while number is True
    n += 1
    print(n)

# 5. Make an infinite loop using WHILE LOOP.
n = 1
v = 1
while n:  # while number is True
    v += 1
    print('∞ ', v)

# Thank you, Mike!
