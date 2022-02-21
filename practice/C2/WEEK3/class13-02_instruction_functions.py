# FUNCTIONS IN PYTHON

# Creating a Function
# In Python a function is defined using the def keyword:

def friendly_message():
  print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:

friendly_message()

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as function requires, arguments are separated with a comma.

def another_frendly_message(msg, count):
    for i in range(count):
        print(f'{i+1} - {msg}')

another_frendly_message("Hello again from a function", 6)

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

another_frendly_message(count = 3, msg = "We are mixing things up")

# 1. Calculation program using prompt or direct entry
# program where we have a function with additional data (arguments)

# write second
def prompt(n):
    return int(input(f'Enter integer {n}: '))

# write first, addition first then multiplication (after prompt)
def calculation(a, b, c, d):
    print(f' The sum of {a} and {b} is: {a + b}')
    print(f' The product of {c} and {d} is: {c * d}')

# use prompt function to provide value for function arguments
calculation(prompt(1), prompt(2), prompt(3), prompt(4))

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

# create a calculation function
def calc(a, b, sign):
    if sign == '+':
        print(f'The result of addition {a + b}')
    elif sign == '-':
        print(f'The result of subtraction {a - b}')
    elif sign == '*':
        print(f'The result of multiplication {a * b}')
    elif sign == '/':
        print(f'The result of float division {a / b}')
    elif sign == '//':
        print(f'The result of integer division {a // b}')
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

# Create a function to extract a value from the string located between characters
# example 1 extract Moodle User System ID

href = 'http://52.39.5.126/user/view.php?id=1456&course=1'
first = '='
second = '&'
start = href.find(first) + len(first)
end = href.rfind(second)
user_system_id = href[start:end]
print(user_system_id)

# One liner
# user_system_id = href[href.find('=') + 1 : href.rfind('&')]



def find_between(val, first, last):
    try:
        start = val.find(first) + len(first)
        print(f'Start index: {start}')
        end = val.find(last, start)
        print(f'End index: {end}')
        return val[start:end]
    except ValueError:
        return ""

print(find_between('http://52.39.5.126/user/view.php?id=533&course=1','=','&'))

# why to use len(first)
delete_url = 'http://52.39.5.126/admin/user.php?sort=name&dir=ASC&perpage=30&page=0&delete=1456&sesskey=cGzx8Nx2hu'

print(find_between(delete_url,'dir=','&'))


# print(find_between_r('http://52.39.5.126/user/view.php?id=5363','=',))
#
# def find_between_r( s, first, last ):
#     try:
#         start = s.rindex( first ) + len( first )
#         end = s.rindex(last, start)
#         return s[start:end]
#     except ValueError:
#         return ""




