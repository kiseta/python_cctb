import time
from time import sleep
import copy
import random
from faker import Faker

fake = Faker(locale='en_CA')


# PYTHON IMPORT
# In Python, you use the 'import' keyword to make code in one module available in another.
# Imports in Python are important for structuring your code effectively.
# Using imports properly will make you more productive,
# allowing you to reuse code while keeping your projects maintainable.

# 1. TIME
# Python modue called 'time' - add to the top of the file: import time
current_date = time.asctime()
print('~*~*~*~*~*~*~*~*~*~*~*~')
print(f'Test started {current_date}')

seconds = 10
while seconds != 0:
    print(seconds)
    seconds -=1
    sleep(1)

# 2. COPY
# Python module called 'copy'  - add to the top of the file: import copy

name_list = ['Bryan', 'Kate', 'Maria', 'Alice', 'Jayson'] # make a list of items
new_list = copy.copy(name_list)
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
num = int(input('Enter the number of fruits you want to eat: '))
for d in range(num):
    i = input(f'Enter any {num} fruits: ')
    fruit.append(i)
print(f'Random choice is {random.choice(fruit)}')

# define function
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
print(f'Second call ----------------------')
select_fruit()
print(f'Third call ----------------------')
select_fruit()

# External Python library called 'Faker'
# to use, requires 3 steps:
# Step 1 Instal Faker Library via Python Packages installer
# Step 2 Add to the top of the file: from faker import Faker
# Step 3 create a variable and set the locale: fake = Faker(locale='en_CA')
# To use:
email = fake.email()
print(email)
address = fake.address()#.replace('\n', " ")
print(address)
