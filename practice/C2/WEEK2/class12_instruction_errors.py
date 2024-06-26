__author__ = 'tk'
# PYTHON TRY AND EXCEPT
# try, except, finally - are keywords related to errors and exceptions block
# try - block where you try to run some piece of code
# except - block where we can handle the error
# else - block where there is no error
# finally - block what happens at the end, where  you can say somethign about the code
# break - stops program from executing futher

# 1. Program to check integers
user_entry = None
while type(user_entry) != int:
    try:
        user_entry = int(input('Please enter an integer: '))
        print(f'You entered integer: {user_entry}. Program finished.')
    except ValueError as e:
        print(f'You entered incorrect value. Please try again!')
        print(f'Error message: ', e)

# 2.Program to check the number from the given range
# Program requirements
# Check if entry is an integer
# Check if the entry is in range
# Keep prompting to enter a number until the correct value is entered

# solution 2.1
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

# solution 2.2
numbers = None
valid_flag = False
while not valid_flag:
    try:
        numbers = int(input('Please enter any integer number from 1 to 10: '))
        while 0 < numbers <= 10:
            print(f'All good. Your number {numbers} is from 1 to 10.')
            valid_flag = True
            break
        else:
            print(f'Your number {numbers} is not from a given range. Please try again!')
    except ValueError as e:
        print(f'You entered non integer value. Please try again! Error message: ', e)
    finally:
        print('End program!')

# 3. Program where we can try to divide by 0.

try:
    x = int(input('Enter numerator: '))
    y = int(input('Enter denominator: '))
    print(f'Answer is {round(x / y)}')
# except (ValueError, ZeroDivisionError) as e:
#     print(f'Error occurred. Error message: ', e)
except ZeroDivisionError as zero:
    print(f'You can\'t divide by zero - {zero}')
except ValueError as value:
    print(f'You entered a non-integer value - {value}')
finally:
    print('Program is done')

# 4.
# NameError: name 'pam' is not defined

ages = {
    'Pam': 99,
    'jim': 24,
    'michael': 43
}

print(f'Michael is {ages["michael"]} years old.')
person = input(f'Please enter name: ')
try:
    print(f'{ages[person]}')
except NameError as n:
    print(n)


# EXAMPLE 1 List IndexError
try:
    twilight_saga = ['Twilight', 'New Moon', 'Eclipse', 'Breaking Dawn']  # make a list with square brackets
    print(twilight_saga)
    print('--------- correct - twilight_saga[3] ------------')
    print(twilight_saga[3]) # print 4TH item from the list using zero based index
    print('--------- error - twilight_saga[4] ------------')
    print(twilight_saga[4])  # print 4TH item from the list - generate error
except IndexError as ie:
    print(f'IndexError: {ie}, check your item index')
finally:
    print('---------------- Program is done----------------')


# example TypeError (already highlighted in the code) or ValueError
val1 = input('enter value 1: ')
val2 = input('enter value 2: ')
print(val1 / val2)

try:
    print(val1 / val2)
except TypeError as te:
    print(f'This operation is not allowed')




def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

print(find_between_r('http://52.39.5.126/user/view.php?id=533&course=1','=','&'))



