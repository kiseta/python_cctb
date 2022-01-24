__author__ = 'tk'
# LIST
list_of_something = []

# TUPLE
# Tuple is a collection which is ordered and unchangeable. Allow duplicate members
# Tuples are used to store multiple items in a single variable.
# Tuples are written with round brackets

yummy_tuple = ("apple", 'banana', 'cherry', 'mango', 'watermelon')

# Access tuple items - let's get the second one
print(yummy_tuple[1])

# Get the last value from the tuple
print(yummy_tuple[-1])

# Tuples are unchangeable, meaning you cannot change, add, or remove items once tuple is created
# Array of constants! (c Tatyana)
# But it's possible to convert tuple into a list, then make changes and then convert it back using tuple() method

# SET
# Set is a collection which is unordered, unchangeable and unindexed. No duplicate members.
# Sets are written in curly brackets.

yummy_set = {"apple", 'banana', 'cherry', 'mango', 'watermelon'}
print(yummy_set)

for y in yummy_set:
    print(y)

# DICTIONARY
# Dictionary is a collection which is ordered and changeable. No duplicate members.
music_technica = {
    'brand': 'SONY',
    'type': 'Receiver',
    'model': 'ST090GH',
    'year': 2020
}

# Display all
print(music_technica)

# Display only keys, not values
print(music_technica.keys())

# Display keys and values as dict_items container
print(music_technica.items())

# Display only values, not the keys
print(music_technica.values())

# Display info about my key - what's inside?!
print(music_technica.get('brand'))

# Change the value of 'brand' key
music_technica['brand'] = 'Yamaha'
print(music_technica)

#####################################
# CONDITIONAL STATEMENTS
# COMPARISON OPERATORS TABLE
# < - less than
print(3 < 5)  # if 3 is less than 5

# <= - less than or equals
print(6 <= 9)

# > - more (greater) than
print(10 > 2)

# >= - more (greater) or equals
print(24 >= 23)

# == is equals
print(5 == 5)

# != is not equals to
print(8 != 1)

# IF Conditional statement
age = int(input('Enter your age: '))
if 40 > age > 20:
    print('Your age is greater than 20. Not bad!')
elif 5 < age < 10:
    print('Your age is less than 10. Well done!')
elif age == 0:
    print('You\'ve not born yet. Please wait a couple of month!')
else:
    print(f'Your age isn\'t defined and it is {age}')

# Check the nationality
nationality = input('What is your nationality? '
               'Type english, french, italian, chinese, indian, korean, russian, kazakh, uzbek, ukrainian : ')

age = int(input('Enter your age: '))
if nationality == 'english' and age < 15:
    print('I\'m gonna say Heyyy to you')
elif nationality == 'english' and age > 15:
    print('I\'m gonna say Hello to you')
elif nationality == 'french':
    print('I\'m gonna say Bonjour to you')
elif nationality == 'italian':
    print('I\'m gonna say Chao to you')
elif nationality == 'chinese':
    print('I\'m gonna say nÄ­ hÄƒo to you')
elif nationality == 'indian':
    print('I\'m gonna say Namaste to you')
elif nationality == 'korean':
    print('I\'m gonna say annyeonghaseyo to you')
elif nationality == 'russian':
    print('I\'m gonna say ÐŸÑ€Ð¸Ð²ÐµÑ‚ to you')
elif nationality == 'kazakh' or nationality == 'uzbek':
    print('I\'m gonna say Salam to you')
elif nationality == 'ukrainian':
    print('I\'m gonna say ÐŸÑ€Ð¸Ð²Ñ–Ñ‚ to you')
else:
    print(f'Sorry, I can\'t recognize what is {nationality} nationality')

