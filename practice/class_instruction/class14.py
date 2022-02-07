__author__ = 'tk'
import copy
import random
from random import randint, uniform
from time import sleep, asctime

current_date = asctime()
print(f'------------------------')
print(f'Test started {current_date}')

seconds = 10
while seconds != 0:
    print(seconds)
    seconds -= 1
    sleep(1)

# Python module called 'copy'
ninjago = ['Lloyd', 'Kai', 'Nya', 'Cole', 'Zane', 'Jay']
new_list = copy.copy(ninjago)
print(new_list)

# Python module random
# Method to generate random integer numbers is RADNINT
a = randint(1000, 1000000)
print(f'The random int number is {a}')

# Program to generate random int numbers based on user input
x = int(input('Enter number for the lowest value in range: '))
y = int(input('Enter number for the highest value in range: '))
z = randint(x, y)

print(f'The lowest and highest values in range are {x, y}')
print(f'The random dynamic int number is {z}')

# Program to generate float numbers using random module/library
f = uniform(1.5, 7.5)
print(f'The random float number is {f}')

# Program to generate random float numbers based on user's input
start_n = float(input('Enter number for the lowest value in range: '))
stop_n = float(input('Enter number for the highest value in range: '))
float_number = uniform(start_n, stop_n)

print(f'The lowest and highest values in range are {start_n, stop_n}')
print(f'The random dynamic float number is {float_number}')


# Python choice method from the random library
list_of_all = ['Moodle', 38, True, 25.0, 'Python']
print(f'My choice from this list is {random.choice(list_of_all)}')

# Program will generate list of values based on user's input and pick a random value
fruits = []
numbers_of_elements = int(input('How many fruits are in the basket?: '))
for d in range(numbers_of_elements):
    i = input(f'Enter name of the fruit {d}+1: ')
    fruits.append(i)
print(f'Random choice is {random.choice(fruits)}')

#---------------------------- FUNCTIONS -----------------------------------------------------------------

# Function definition
def pick_dessert():
    desserts = []
    numbers_of_elements = int(input('How many desserts are on the menu: '))
    for d in range(numbers_of_elements):
        i = input(f'Enter choice number {d}+1: ')
        desserts.append(i)
    print(f'Random choice is {random.choice(desserts)}')


# Function call
print(f'First call')
pick_dessert()
print(f'Second call')
pick_dessert()
print(f'Third call')
pick_dessert()

# CTRL+D - duplicate on Windows PC
# CMD+D - duplicate on Mac


# Function definition
def pick_fruit():
    fruit_list = []
    total = int(input('How many fruits are in the basket?: '))
    for d in range(total):
        i = input(f'Enter name of the fruit {d}+1: ')
        fruit_list.append(i)
    print(f'Thank you! Your random fruit today is:')
    print(f'Random fruit: {random.choice(fruit_list)}')


# Function call
print(f'First call')
pick_fruit()
print(f'Second call')
pick_fruit()
print(f'Third call')
pick_fruit()

# CTRL+D - duplicate on Windows PC
# CMD+D - duplicate on Mac


def prompt():
    return int(input('Enter any number: '))


# Program where we have a function with additional data (arguments)
def addition(a, b, c, d):
    print(f'The sum of two arguments will be {a + b}')
    print(f'The multiplication of two arguments will be {c * d}')


addition(prompt(), prompt(), prompt(), prompt())


def calculation(a, b, c):
    print(f'Result {a + b - c}')


calculation(3, 10, 5)
calculation(100000, 91878787, 787878787)

sign = input('Enter a sign operator: ')


def calc(a, b, sign):
    if sign == '+':
        print(f'The result of addition is {a + b}')
    elif sign == '-':
        print(f'The result of subtraction is {a - b}')
    elif sign == '*':
        print(f'The result of multiplication is {a * b}')
    elif sign == '/':
        print(f'The result of float division is {a / b}')
    elif sign == '//':
        print(f'The result of integer division is {a // b}')
    else:
        print(f'Something is wrong. Please check your arguments')


# Cal function call
calc(5, 5, sign)