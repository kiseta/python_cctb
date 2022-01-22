__author__ = 'tk'
# PYTHON TRY AND EXCEPT
# try, except, finally - are keywords related to errors and exceptions block
# try - block where you try to run some piece of code
# except - block where we can handle the error
# else - block where there is no error
# finally - block what happens at the end, where  you can say somethign about the code

# 1. Program to check integers
# user_entry = None
# while type(user_entry) != int:
#     try:
#         user_entry = int(input('Please enter an integer: '))
#         print(f'You entered integer: {user_entry}. Program finished.')
#     except ValueError as e:
#         print(f'You entered incorrect value. Please try again!')
#         print(f'Error message: ', e)

# 2.Program to check the number from the given range
# Program requirements
# Check if entry is an int
# Check if the entry is in range
# Keep prompting to enter a number until the correct value is entered

# numbers = None
# while type(numbers) != int:
#     try:
#         numbers = int(input('Please enter any integer number from 1 to 10: '))
#         while 0 <= numbers <= 10:
#             print(f'All good. Your number is from the given range')
#             break
#         else:
#             print(f'Your number {numbers} is not from a given range. Please try again!')
#     except ValueError as e:
#         print(f'You entered non integer value. Please try again!')
#         print(f'Error message: ', e)

# 3. Program where we can try to divide by 0.

# try:
#     x = int(input('Enter numerator: '))
#     y = int(input('Enter denominator: '))
#     print(f'Answer is {round(x / y)}')
# # except (ValueError, ZeroDivisionError) as e:
# #     print(f'Error occurred. Error message: ', e)
# except ZeroDivisionError as zero:
#     print(f'You can\'t divide by zero - {zero}')
# except ValueError as value:
#     print(f'You entered a non-integer value - {value}')
# finally:
#     print('Program is done')

# 4.


#NameError: name 'boooks' is not defined

# ages = {
# 	'pam': 24,
# 	'jim': 24,
# 	'michael': 43
# }
#
# print(f'Michael is {ages["michael"]} years old.')

# 2.Program to check the number from the given range
# Program requirements
# Check if entry is an int
# Check if the entry is in range
# Keep prompting to enter a number until the correct value is entered

numbers = None
invalid_flag = True
while invalid_flag:
    try:
        numbers = int(input('Please enter a number from 1 to 10: '))
        while 0 < numbers <= 10:
            print(f'All good. Your number {numbers} is from 1 to 10.')
            invalid_flag = False
            break
        else:
            print(f'Your number {numbers} is not from a given range. Please try again!')
            invalid_flag = True
    except ValueError as e:
        print(f'You entered non integer value. Please try again!')
        print(f'Error message: ', e)
        invalid_flag = True
