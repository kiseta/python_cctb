# yummy_tuple = ('apple', 'banana', 'mango', 'cherry', 'apple','banana', 'apple')
# yummy_list = ['apple', 'banana', 'mango', 'cherry', 'apple','banana', 'apple']
#
# print(yummy_tuple.count('apple'))
# print(len(yummy_tuple))
# print(yummy_tuple[5])
#
# for f in yummy_tuple:
#     print(f)
#
# for fr in yummy_list:
#     print(fr)
#
#
# # 2. Program to check the numbers from the given range
# numbers = None
# integer = None
# string = None
#
# while (not integer) and (not string):
#     try:
#         numbers = int(input('Enter any number from 1 to 10: '))
#         while 0 < numbers <= 10:
#             print(f'All good. Number is from 1 to 10.')
#             integer = True
#             break
#         else:
#             print(f'You entered value not from the given range!')
#             string = False
#     except ValueError as e:
#         print(f'You entered string value, not integer. Try again!')
#     finally:
#         print('Program is done')

# pi = 3.14159
# print('Print %s' % 'Hello, World!')
# print('%.2f' % pi)
# print('%f' % pi)

########################################################
# # Task 4. We want to control float number decimals
# given_float_number = 14.9873492873
#
# # TREE METHODS TO CONTROL DECIMALS
# print(round(given_float_number, 2)) # METHOD 1
# print("{:.2f}".format(given_float_number)) # METHOD 2
# print('Method ot print using %s  ' % '\'percentage sign s string formatter\'')
# print('%f' % given_float_number) # METHOD 3
# print('%.2f' % given_float_number) # METHOD 4
#
# b = c = d = e = int(input('Enter year: '))  # Dynamic Values
# print(b, c+1, d+2, e+3)

# Python Modulo Operator (Remainder)
# The modulus operator, sometimes also called the remainder operator (or integer remainder operator)
# works on integers (and integer expressions) and yields the remainder when the first operand is divided by the second.
# In Python, the modulus operator is a percent sign ( % )
# How much will remain of the first number after the second number
# fits into it the maximum number of times
# print(10 % 4)
# print(15 % 12)
# print(98 % 9)

# # create a tuple
# yummy_tuple = ('apple', 'banana', 'mango', 'cherry', 'watermelon')
# print(yummy_tuple)
#
# # print second item from the tuple (remember starts with zero)
# print(yummy_tuple[1])
#
# # update tuple
# yummy_list = list(yummy_tuple) # to change a tuple, cast it into list using list() function
#
# # append and item
# yummy_list.append('grapes')
# print(yummy_list)
#
# # remove an item
# yummy_list.pop(4)
# print(yummy_list)
#
# # convert back to tuple
# yummy_tuple = tuple(yummy_list)
# print(yummy_tuple)
#
# # print items on new line using for loop
# for yt in yummy_tuple:
#     print(yt)
#
# # Using for loop print index : value pairs from a list or tuple
# tropical_tuple = ('Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee')
#
# for i in range(len(tropical_tuple)):
#     print(f'{i} : {tropical_tuple[i]}')
#
# # Using for loop print index : value pairs from a list or tuple
# tropical_list = ['Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee']
#
# for i in range(len(tropical_list)):
#     print(f'{i} : {tropical_list[i]}')

# IF Conditional statement
# print(f'Welcome to our website! We can help you pick the right game for your age.')
# age = int(input('Please enter your age: '))
# if age > 20 and age <= 40:
#     print('Your age is 20 to 40. Not bad! You can play the following games: G1, G2, G3')
# elif age > 11 and age <= 20:
#     print('Your age is 11 to 20. Cool! We suggest these games for you: G4, G5, G6')
# elif age > 5 and age <= 10:
#     print('Your age is 5 to 10. Awesome! Let\'s play these games: G-01, G-02, G-03')
# elif age == 0:
#     print('You\'re not born yet. Please wait for a few years!')
# else:
#     print(f'We don\'t have any games for your age: {age}')

# IF Conditional statement
# print(f'Welcome to our website! We can help you pick the right game for your age.')
# age = int(input('Please enter your age: '))
# if 20 <= age < 40:
#     print('Your age is 20 to 40. Not bad! You can play the following games: G1, G2, G3')
# elif 10 <= age < 20:
#     print('Your age is 11 to 20. Cool! We suggest these games for you: G4, G5, G6')
# elif 5 <= age < 10:
#     print('Your age is 5 to 10. Awesome! Let\'s play these games: G-01, G-02, G-03')
# elif age == 0:
#     print('You\'re not born yet. Please wait for a few years!')
# else:
#     print(f'We don\'t have any games for your age: {age}')

a = [1, 2, 3, 'a', 1, 3, 5] # create list
# print(a)
# print(tuple(a))
# print(set(a))
#
# b = {'a', 1, 4, 8} # create set
# print(b)
# print(list(b))
# print(tuple(b))
# print(dict.fromkeys(a,1))


# Make Dictionary from 2 lists
key_lst= ['username', 'password', 'firstname','lastname', 'email']
val_lst = ['testuser99', 'Pass1', 'Test','User', 'testuser99@google.com']

dic_lst = {key_lst[i]: val_lst[i] for i in range(len(key_lst))}
print(dic_lst)
print(len(dic_lst))

