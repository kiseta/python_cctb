__author__ = 'tk'
# Data types / objects in Python

# LIST
# LIST - List or Array is an object to store multiple values. Starts with zero (0)
# list is a collection that is ordered and changeable
list_of_something=[] # make a list with square brackets

list_of_names = ['Jack',  'Sparrow',  'Nina',  'Bruce',  'Justin',  'Tatyana']
print(list_of_names)

# read values by calling a specific index
print(list_of_names[0])

# update value in the list
list_of_names[0] = 'George'
print(list_of_names)

# append
list_of_names.append('Nona')
print(list_of_names)

# remove value
list_of_names.pop(0)
print(list_of_names)

# clear
#list_of_names.clear()
print(len(list_of_names))

# ---------------------------------------------------------
# TUPLE
# Tuples are unchangeable, you cannot change,  add, remove items from the tuple.
# It's possible to convert tuple into a list, then make  changes and then convert it back tuple
# array of constants
# Tuple is a collection that is ordered and unchangeable.
# Allow duplicate members
# Tuples are used to store multiple items in a single variable
# Tuples are written with round () brackets

yummy_tuple = ('apple', 'banana', 'mango', 'cherry', 'watermelon')
print(yummy_tuple)
print(yummy_tuple[1])
yummy_list = list(yummy_tuple)
print(yummy_list)

yummy_list.append('nectarine')
print(yummy_list)
yummy_tuple = tuple(yummy_list)
print(yummy_tuple)
print('----------------------')
# SET
# Set is unordre, unchangable and unindexed. No duplicate memebers
# Sets are written in curly brackers

yummy_set = {'apple', 'banana', 'mango', 'cherry', 'watermelon'}
print(yummy_set)

for ys in yummy_set:
    print(ys)

# DICTIONARY
# Dictionary is a collection which is ordered, changeable, no duplicate members
#
music_technica ={
    'brand': 'sony',
    'type': 'receiver',
    'model': 'ST090GH',
    'year': 2020
}
new_user = {
    'username': 'testuser',
    'password': 'Pass1',
    'firstname': 'Test',
    'lastname': 'User',
    'emailaddress': 'testuser@gmail.com'
}

# Display all
print(music_technica)
print(new_user)

# keys only
print(music_technica.keys())
print(new_user.keys())

# keys and values as dict_items container
print(music_technica.items())
print(new_user.items())

# values only
print(music_technica.values())
print(new_user.values())

# Display values for the key
print(music_technica.get('brand'))
print(new_user.get("password"))

# Change the value of key
#method 1
music_technica.update({'type': 'TV'})
new_user.update({'password': 'Pswd3!'})

print(music_technica)
print(new_user)

music_technica['brand'] = 'Yamaha'
new_user['username'] = 'happyuser'

print(music_technica)
print(new_user)
