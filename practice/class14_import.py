__author__ = 'tk'
import time
from time import sleep
import copy
import random

# current_date = time.asctime()
# print('~*~*~*~*~*~*~*~*~*~*~*~')
# print(f'Test started {current_date}')
#
# seconds = 10
# while seconds != 0:
#     print(seconds)
#     seconds -=1
#     sleep(1)


# Python module called 'copy'

# ninjago = ['Lloyd', 'Kai', 'Nya', 'Cole', 'Jay'] # make a list of items
# new_list = copy.copy(ninjago)
# print(new_list)

# Python module called 'random'
# method to generate random integer numbers is RANDINT
# a = random.randint(1111,9999)
# print(f'The random int is {a}')

# Program to generate random integers based on user input
# x = int(input('Enter a number for the lowest value in range: '))
# y = int(input('Enter a number for the highest value in range: '))
# z = random.randint(x,y)
#
# print(f'Generate random integer from to {x, y}')
# print(f'The random dynamic int number is: {z}')

# Program to generate float number using random/library
# f = random.uniform(1.5, 7.5)
# print(f'The random float number is: {f}')
#
# # Program to generate random float numbers based on user input
# start_n = float(input('Enter a number for the lowest value in range: '))
# stop_n = float(input('Enter a number for the highest value in range: '))
# float_n = random.uniform(start_n, stop_n)
#
# print(f'Generate random integer from to {start_n, stop_n}')
# print(f'The random dynamic int number is: {float_n}')

#Program will generate list of values based on user's input
# fruit = []
# num = int(input('Enter the number of fruits you want to eat: '))
# for d in range(num):
#     i = input(f'Enter any {num} fruits: ')
#     fruit.append(i)
# print(f'Random choice is {random.choice(fruit)}')

# define function
def select_fruit():
    fruit = []
    num = int(input('Enter the number of fruits you have: '))
    for d in range(num):
        i = input(f'Enter fruit {d+1} of {num}: ')
        fruit.append(i)
    print(f'Random choice is {random.choice(fruit)}')

# call function
# print(f'First call ----------------------')
# select_fruit()
# print(f'Second call ----------------------')
# select_fruit()
# print(f'Third call ----------------------')
# select_fruit()


