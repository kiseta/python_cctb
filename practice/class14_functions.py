__author__ = 'tk'

# program where we have a function with additional data (arguments)

# write second
def prompt(n):
    return int(input(f'Enter integer {n}: '))

# write first, addition first then multiplication (after prompt)
def addition(a, b, c, d):
    print(f' The sum of {a} and {b} is: {a + b}')
    print(f' The product of {c} and {d} is: {c * d}')

#addition (1, 3) # before adding multiplicaton
addition(prompt('a'), prompt('b'), prompt('c'), prompt('d'))

def calculations(a, b, c):
    print(f'Result of {a} + {b} - {c} is: {a + b - c}')

calculations(prompt('a'), prompt('b'), prompt('c'))


# Program display a message multiple times using function and

def display_message(n):
    for i in range(n):
        print('Hello, World!')

print('This program will display a message as many times as you want: ')
display_message(int(input(f'Enter a number: ')))


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
calc(prompt('a'), prompt('b'), input(f'Enter sign operator: '))
# Subtraction
calc(prompt('a'), prompt('b'), input(f'Enter sign operator: '))
# Multiplication
calc(prompt('a'), prompt('b'), input(f'Enter sign operator: '))
# Division
calc(prompt('a'), prompt('b'), input(f'Enter sign operator: '))
# Division
calc(prompt('a'), prompt('b'), input(f'Enter sign operator: '))


def calculations1(a, b, c, d):
    print(f'Result {(a + b - c) * d}')

numlist = [3, 5, 7, 9]
print(numlist)
calculations1(*numlist) # use * arguments unpacking operator

def pass_collection(a, b, c, d):
  print(a, b, c, d)

l = [0, 1]
d = {"c":3, "d":2}

pass_collection(*l, **d)  # pass collection using * unpacking operator
