import random
import time
from copy import copy
from time import sleep

from faker import Faker

fake = Faker(locale='en_CA') # initialize the external library

# PYTHON ERROR HANDLING REVIEW

# step 1 define program requirements
# Integer division program requirements:
# program requires 2 numbers
# step 2 create a basic program
# step 3 test your program with all possible inputs (hardcoded):
# correct input (integers within the range), incorrect input: letters, and zero, negative numbers are ok
# determine the error codes: ValueError
# once your program is tested and working use the try, except finally statement as follows:
# your program goes into try: block
# error code(s) go into except: block(s)
# test your program again to confirm the errors are being caught and handled.
# print user-friendly messages to inform of the results.

print(f'Welcome to division program, where we can divide two numbers.')
try:
    x = int(input('Enter number 1: numerator: '))
    y = int(input('Enter number 2: denominator: '))
    print(f'Answer is {round(x / y)}')
# except (ValueError, ZeroDivisionError) as e:
#     print(f'Error occurred. Error message: ', e)
except ZeroDivisionError as zero:
    print(f'You can\'t divide by zero - {zero}')
except ValueError as value:
    print(f'You entered a non-integer value - {value}')
finally:
    print('Program is finished!')

#_______________________________________________________________________

# PYTHON IMPORT
# In Python, you use the 'import' keyword to make code in one module available in another.
# Imports in Python are important for structuring your code effectively.
# Using imports properly will make you more productive,
# allowing you to reuse code while keeping your projects maintainable.

# 1. TIME
# Python module called 'time' - add to the VERY top of the file: import time

current_date = time.asctime()
print('-----------------------------')
print(f'Test Started: {current_date}')

# create a ticking timer using sleep() function, add to the top of the file: from time import sleep
# prompt = print(input('Initiate self-destruct? (Yes/No)'))
#
# if prompt == 'Yes':
seconds = 10
while seconds != 0:
    print(f'Time to self-destruct: {seconds} sec')
    seconds -= 1
    # seconds -=1
    sleep(1) # requires import: add to top of the file: from time import sleep

print(f'🌟🌟🌟 BOOM! 🌟🌟🌟')
# else:
#     print(f'Self-distract aborted!')

# 2. COPY
# Python module called 'copy'  - add to the top of the file: import copy

name_list = ['Bryan', 'Kate', 'Maria', 'Alice', 'Jayson'] # make a list of items
new_list = copy(name_list)
print(new_list)

# 3. RANDOM

# Python module called 'random'  - add to the top of the file: import random
# method to generate random integer numbers is RANDINT
a = random.randint(1111,9999)
print(f'The random int is {a}')

# Program to generate random integers based on user input
x = int(input('Enter a number for the lowest value in range: '))
y = int(input('Enter a number for the highest value in range: '))
z = random.randint(x,y)

print(f'Generate random integer from to {x, y}')
print(f'The random dynamic int number is: {z}')

# Program to generate float number using random/library
f = random.uniform(1.5, 7.5)
print(f'The random float number is: {f}')

# Program to generate random float numbers based on user input
start_n = float(input('Enter a number for the lowest value in range: '))
stop_n = float(input('Enter a number for the highest value in range: '))
float_n = random.uniform(start_n, stop_n)

print(f'Generate random integer from to {start_n, stop_n}')
print(f'The random dynamic int number is: {float_n}')

# Program will generate list of values based on user's input
fruit = []
num = int(input('Enter the number of fruits you have: '))
for d in range(num):
    i = input(f'Enter fruit {d + 1} of {num}: ')
    fruit.append(i)
print(f'Random choice is {random.choice(fruit)}')

# transfer the code above to the function
def select_fruit():
    fruit = []
    num = int(input('Enter the number of fruits you have: '))
    for d in range(num):
        i = input(f'Enter fruit {d + 1} of {num}: ')
        fruit.append(i)
    print(f'Random choice is {random.choice(fruit)}')

# call function
print(f'First call ----------------------')
select_fruit()
# print(f'Second call ----------------------')
# select_fruit()
# print(f'Third call ----------------------')
# select_fruit()

# External Python library called 'Faker'
# to use, requires 3 steps:
# Step 1 Instal Faker Library via Python Packages installer
# Step 2 Add to the top of the file: from faker import Faker
# Step 3 Initialize the library - create a variable and set the locale: fake = Faker(locale='en_CA')
# To use:
email = fake.email()
print(email)
address = fake.address()#.replace('\n', " ")
print(address)
print(address.replace('\n', " "))

username = fake.user_name()
print(username)

password = fake.password(length=30)


# num = 33
# rng = 3
# program to generate password based on user input
print('------------------PROGRAM TO GENERATE PASSWORD BASED ON USER INPUT USING FOR LOOP-----------------\n')

num = int(input(f'Please enter the number of characters for your password: '))
rng = int(input(f'How many passwords do you want?: '))
for i in range(rng):
    pwd = fake.password(length=num)
    print(f'Here is your {num} character long password {i + 1} of {rng}: {pwd}')
else:
    print(f'Passwords generation is done!')

# print('\n------------------PROGRAM TO GENERATE PASSWORD BASED ON USER INPUT USING WHILE LOOP-----------------\n')
# num = int(input(f'Please enter the number of characters for your password: '))
# total = int(input(f'How many passwords do you want?: '))
# cntr = 1
# while total != 0:
#     pwd = fake.password(length=num)
#     print(f'Here is your {num} character long password {cntr} of {total}: {pwd}')
#     total -= 1
#     cntr += 1
# else:
#     print(f'Passwords generation is done!')


print('\n------------------PROGRAM TO GENERATE PASSWORD BASED ON USER INPUT USING FOR LOOP-----------------\n')

try:
    num = int(input(f'Please enter the number of characters for your password: '))
    rng = int(input(f'How many passwords do you want?: '))
    for i in range(rng):
        pwd = fake.password(length=num)
        print(f'Here is your {num} character long password {i + 1} of {rng}: {pwd}')
    else:
        print(f'Passwords generation is done!')
except ValueError as value:
    print(f'You entered a non-integer value - Error: {value}. Try again!')
except AssertionError as value:
    print(f'You entered incorrect value - Error: {value}. Try again!')
finally:
    print('Program is finished!')


try:
    print('------------------PROGRAM TO GENERATE PASSWORD BASED ON USER INPUT USING WHILE LOOP-----------------\n')
    num = int(input(f'Enter the number of characters for your password: '))
    total = abs(int(input(f'How many passwords do you want?: ')))
    cntr = 1
    while total != 0:
        pwd = fake.password(length=num)
        print(f'Here is your {num} character long password {cntr} of {total}: {pwd}')
        total -= 1
        cntr += 1
    else:
        print(f'Passwords generation is done!')
except ValueError as value:
    print(f'You entered a non-integer value - Error: {value}. Try again!')
except AssertionError as value:
    print(f'You entered incorrect value - Error: {value}. Try again!')
finally:
    print('Program is finished!')