__author__ = 'tk'

# Lab Assignment 11 - Errors

# 1. Create a program in Python and use try and catch.
# 2. Simulate error and catch it using except.
# 3. Use finally keyword to finalize the statement.

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

# 2.Program to check the number from the given range
# Program requirements
# Check if entry is an intteger
# Check if the entry is in range
# Keep prompting to enter a number until the correct value is entered

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
        print('The program is done!')