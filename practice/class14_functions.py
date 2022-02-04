__author__ = 'tk'

# program where we have a function with additional data (arguments)

# write second
def prompt():
    return int(input('Enter a number: '))

# write first, addition first then multiplication (after prompt)
def addition(a, b, c, d):
    print(f' The sum of two arguments a and b is: {a + b}')
    print(f' The product of arguments c and d is: {c * d}')

#addition (1, 3) # before adding multiplicaton
addition(prompt(), prompt(), prompt(), prompt())

def calculations(a, b, c):
    print(f'Result {a + b - c}')

calculations(3, 10, 999)

def display_message(n):
    for i in range(n):
        print('Hello, World!')

display_message(5)


def calc(a, b, sign):
    if sign == '+':
        print(f'The result of addition {a + b}')
    elif sign == '-':
        print(f'The result of substrcation {a - b}')
    elif sign == '*':
        print(f'The result of multiplication {a * b}')
    elif sign == '/':
        print(f'The result of float division {a / b}')
    elif sign == '//':
        print(f'The result of interger division {a // b}')
    else:
        print(f'Something is wrong. Please check your arguments {a, b, sign}')

# Addition
calc(5, 5, input(f'Enter sign operator: '))
# Subtraction
calc(5, 5, input(f'Enter sign operator: '))
# Multiplication
calc(5, 5, input(f'Enter sign operator: '))
# Division
calc(5, 5, input(f'Enter sign operator: '))
# Division
calc(5, 5, input(f'Enter sign operator: '))


def calculations(a, b, c, d):
    print(f'Result {(a + b - c) * d}')

numlist = [3, 5, 7, 9]
calculations(*numlist) # use * arguments unpacking operator

def foo(a, b, c, d):
  print(a, b, c, d)

l = [0, 1]
d = {"c":3, "d":2}

foo(*l, **d)