__author__ = 'tk'
# PYTHON TRY and EXCEPT
# try, except, finally = keywords
# try - block where you can try to run some piece of code
# except - block where we can handle the error
# else - block where there's no error
# finally - block where you can say something about your code

# 1. Program to check integers
user_enter = None
while type(user_enter) != int:
    try:
        user_enter = int(input('Enter an integer, please: '))
        print(f'You enter {user_enter}. Program finished.')
    except ValueError as e:
        print(f'You entered incorrect value. Try again!')

# 2. Program to check the numbers from the given range
numbers = None
integer = None
string = None

while (not integer) and (not string):
    try:
        numbers = int(input('Enter any number from 1 to 10: '))
        while 0 < numbers <= 10:
            print(f'All good. Number is from 1 to 10.')
            integer = True
            break
        else:
            print(f'You entered value not from the given range!')
            string = False
    except ValueError as e:
        print(f'You entered string value, not integer. Try again!')


# 3. Program where we can try to divide by 0.
try:
    x = int(input('Enter numerator: '))
    y = int(input('Enter denominator: '))
    print(f'Answer is {round(x / y)}')
except ZeroDivisionError as zero:
    print(f'You can\'t divide by zero - {zero}')
except ValueError as value:
    print(f'You entered non-integer value - {value}')
# except (ZeroDivisionError, ValueError) as e:
#     print(f'Errors were happen. Ask your lead about support')
finally:
    print('Program is done')