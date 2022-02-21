__author__ = 'tk'
import copy
import random
import time
from time import sleep

from faker import Faker

fake = Faker(locale='en_CA') # create a variable and initialize the library

# PYTHON IMPORT

# In Python, you can use 'import' keyword to make code from one module avaliable in another
# Imports in Python are important for structuring your code effectively.
# using imports will make you more productive
# make your code more maintanable

# 1. TIME
# Python module called 'time' - add to the VERY top of the file: import time

current_date = time.asctime()
print('-----------------------------')
print(f'Test Started: {current_date}')

# create a ticking timer
seconds = 10
while seconds != 0:
    print(f'Time to self-destruct: {seconds} sec')
    seconds = seconds - 1
    # seconds -=1
    sleep(1) # requires import: add to top of the file: from time import sleep

print(f'🌟🌟🌟 BOOM! 🌟🌟🌟')

# 2. COPY
# Python module called 'copy' - add to the top of the file: import copy

name_list = ['Bryan', 'Kate', 'Maria', 'Alice', 'Jason']
new_list = copy.copy(name_list)
print(new_list)

# 3. RANDOM

# Python module called 'random' - add to the top of the file: import random
# method to generate random integer numbers is random.randint()

a = random.randint(111, 999)
print(f'The random integer is: {a}')
print('testuser' + str(a))

# Program to generate random integers based on user input
x = int(input(f'Enter integer for the lowest value in range: '))
y = int(input(f'Enter integer for the highest value in range: '))
z = random.randint(x, y)

print(f'Generate random integer from {x} to {y}')
print(f'The random integer is: {z}')

# method to generate random floating point numbers is random.uniform()
# Program to generate random float number using random library
f = random.uniform(1.5, 13.3)
print(f'The random float number: {f:.2f}')

# Program to generate random float number based on user input
m = float(input(f'Enter a number for the lowest value in range: '))
n = float(input(f'Enter a number for the highest value in range: '))
r = random.uniform(m, n)

print(f'Generate random float from {m} to {n}')
print(f'The random float is: {r}')

# method to select a random values from the list or a tupple random.choice()
# Program will generate the list of values from user input and then pick the random value

song_list = ['Song 1','Song2','Song3','Song4']
print(f'Random song for today: {random.choice(song_list)}')

fruit = []
num = int(input(f'Enter the number of fruits in the basket: '))
for f in range(num):
    i = input(f'Enter fruit {f + 1} of {num}: ')
    fruit.append(i)

print(f'Random choice is: {random.choice(fruit)}')

# Random library SUMMARY
# random.randint - for random integers
# random.uniform - for random floats
# random.choice - for strings

# EXTERNAL LIBRARY called FAKER
# We are going to use external library called Faker - fake random data generator library for Python
# to use, requires 3 steps:
# Step 1 In PyCharm go to Python Packages and install Faker library
# Step 2 Add to the top of the file: from faker import Faker
# Step 3 Add to the top of the file: fake = Faker(locale='en_CA') - create a variable and set the locale (format of values based on country)
# This will Intialize the library for use in our file

user_name = fake.user_name()

print(user_name)

email = fake.email()

print(email)

password = fake.password()

print(password)

password30 = fake.password(length=30)

print(password30)


# program to generate password based on user input
print('------------------program to generate password based on user input using for loop-----------------')
num = int(input(f'Please enter the number of characters for your password: '))
count = int(input(f'How many passwords do you want?: '))
for i in range(count):
    pwd = fake.password(length=num)
    print(f'Here is your password {i + 1} of {count}: {pwd}')
else:
    print(f'Passwords generation is done!')

print('------------------program to generate password based on user input using while loop-----------------')
num = int(input(f'Please enter the number of characters for your password: '))
count = int(input(f'How many passwords do you want?: '))
i = 1
while count != 0:
    pwd = fake.password(length=num)
    print(f'Here is your password {i + 1} of {count}: {pwd}')
    count -= 1
    i += 1
else:
    print(f'Passwords generation is done!')

