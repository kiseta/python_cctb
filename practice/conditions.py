__author__ = 'tk'
# CONDITIONAL STATEMENTS
# COMPARISON OPERATORS TABLE

# < - less than
print (3 < 5) # if 3 is less than 5

# <=  = less than or equals
print (6 <= 9)

# > more or greater than operator
print (10 > 2)

# >= - greater than or equal
print (24 >= 23)

# == is equal
print(5 == 5)

# != not equal to
print(8 != 1)

if 8 != 1:
    print('old approach')

if not 8 == 1:
    print('new approach')

# IF CONDITIONAL STATMENTS

if 5 == 6:
    print('Yey!')

age = 38
if age > 20:
    print('Your age is greater than 20')

age = int(input('Enter your age: '))
if age > 20:
    print('Your age is greater than 20')
elif age < 10:
    print('Your age is less than 10')
elif age == 0:
    print('You\'ve been born yet. Please wait for couple of month')
else:
    print(f'Your age isn\'t defined and it is {age}')

# Check the nationality

nationality = input('What is your nationality? Type french, italian, chinese, indian, russian, ukranian, kazakh, uzbek')
age = int(input('Enter your age: '))
if nationality == 'french':
    print('I\'m gonna say Bonjour to you')
elif nationality == 'italian':
    print('I\'m gonna say Chao to you')
elif nationality == 'chinese':
    print('I\'m gonna say ni hao to you')
elif nationality == 'indian':
    print('I\'m gonna say Namaste to you')
elif nationality == 'russian' or nationality =='ukranian':
    print('I\'m gonna say Привет to you')
elif nationality =='ukranian':
    print('I\'m gonna say Привiт to you')
elif nationality == 'kazakh'or nationality =='uzbek':
    print('I\'m gonna say Salam to you')
else:
    print(f'Sorry, I can\'t recognise {nationality} nationality')

