# FUNCTIONS IN PYTHON

# 1. Calculation program using prompt or direct entry
def prompt():
    return int(input('Enter a number: '))

def calculation(a, b, c, d):
    print(f'The sum of two arguments is: {a + b}')
    print(f'The product of two arguments is: {c * d}')

# use prompt function to provide value for function arguments
calculation(prompt(), prompt(), prompt(), prompt())

# pass arguments directly
calculation(4, 7, 8, 5)

# pass the list using * - list unpacking operator
num_list = [3, 5, 7, 9]
calculation(*num_list)

# 2. display message n times

def display_message(n):
    for i in range(n):
        print(f'{i} : Hello World!')

display_message(5) # display a message for specified number of times
display_message(prompt()) # use a prompt function to get the value from a use and use it to print as many times