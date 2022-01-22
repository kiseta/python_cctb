__author__ = 'tk'
# EXAMPLE 2 Dictionary - print the first item error
try:
    twilight_character = {
        'vampire': 'Edward',
        'human': 'Bella',
        'werewolf': 'Jacob',
        'hybrid': 'Renesmee'
    }  # make a dictionary with curly braces

    # print('--------- error ------------')
    # print(twilight_character.keys()[0]) # print the value from first type - generate error
    # print('--------- error ------------')
    # print(twilight_character.keys(0)) # print the value from first type - generate error
    print('--------- #2 correct ------------')
    print(twilight_character.get('vampire'))  # print the value from first type
    print(twilight_character.keys())
    print(twilight_character.values())
    print('--------- #2 error ------------')
    # print(twilight_character.keys('vampire'))  # print the value from first key - generate error
    print(twilight_character.values(0))  # print the value from first key - generate error
except TypeError as te:
    print(f'TypeError: {te}, check your item type')
finally:
    print('---------------- Program is done----------------')