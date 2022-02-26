# 1. Create a program in Python and use try, except, finally statement. Simulate error and catch it using
# except keyword. Use finally keyword to finalize the statement.

inventory = {
    'Shirt': 5,
    'Dress': 10,
    'Pants': 15,
    'Shorts': 7,
    'Sweater': 2,
    'Hoodie': 3,
    'Jeans': 4
}

choice = input('What clothes would you like to buy?: ').capitalize()
try:
    print(f'{choice}? Sure! We have {inventory[choice]} of them.')
except KeyError as error:
    print(f'Sorry but we do not have {choice} in our inventory.')
finally:
    print('Thank you for visiting our store!')