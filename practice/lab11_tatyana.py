__author__ = 'tk'
# Lab Assignment 11 - Errors

# 1. Create a program in Python and use try and catch.
# 2. Simulate error and catch it using except.
# 3. Use finally keyword to finalize the statement.

# EXAMPEL 1 List IndexError
try:
    twilight_saga = ['Twilgiht', 'New Moon', 'Eclipse', 'Breaking Dawn']  # make a list with square brackets
    print('--------- correct ------------')
    print(twilight_saga[3])
    print('--------- error ------------')
    print(twilight_saga[4])  # print 4rd item from the list - generate error
except IndexError as ie:
    print(f'IndexError: {ie}, check your item index')
finally:
    print('---------------- Program is done----------------')

# EXAMPEL 2 Dictionary - print the first item error
try:
    twilight_character = {
        'vampire': 'Edward',
        'human': 'Bella',
        'werewolfe': 'Jacob',
        'hybrid': 'Renesmee'
    }  # make a dictionary with curly braces

    print('--------- error ------------')
    print(twilight_character.keys()[0]) # print the value from first type - generate error
    print('--------- error ------------')
    print(twilight_character.keys(0)) # print the value from first type - generate error
    print('--------- correct ------------')
    print(twilight_character.get('vampire'))  # print the value from first type
    print('--------- error ------------')
    print(twilight_character.keys('vampire'))  # print the value from first type - generate error
except TypeError as te:
    print(f'TypeError: {te}, check your item type')
finally:
    print('---------------- Program is done----------------')
