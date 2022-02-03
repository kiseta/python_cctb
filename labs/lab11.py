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

