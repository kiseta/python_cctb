####################################
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

# # IF Conditional statement
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
#
# # Check the nationality
# nationality = input('What is your nationality? '
#                'Type english, french, italian, chinese, indian, korean, russian, kazakh, uzbek, ukrainian : ')
#
# age = int(input('Enter your age: '))
# if nationality == 'english' and age < 15:
#     print('I\'m gonna say Heyyy to you')
# elif nationality == 'english' and age > 15:
#     print('I\'m gonna say Hello to you')
# elif nationality == 'french':
#     print('I\'m gonna say Bonjour to you')
# elif nationality == 'italian':
#     print('I\'m gonna say Chao to you')
# elif nationality == 'chinese':
#     print('I\'m gonna say ni hao to you')
# elif nationality == 'indian':
#     print('I\'m gonna say Namaste to you')
# elif nationality == 'korean':
#     print('I\'m gonna say annyeonghaseyo to you')
# elif nationality == 'russian':
#     print('I\'m gonna say Привет‚ to you')
# elif nationality == 'kazakh' or nationality == 'uzbek':
#     print('I\'m gonna say Salam to you')
# elif nationality == 'ukrainian':
#     print('I\'m gonna say Привiт‚ to you')
# else:
#     print(f'Sorry, I can\'t recognize what is {nationality} nationality')

app = 'Moodle LMS'
# Expected values
app_url = 'http://52.39.5.126/'
home_page_title = 'Software Quality Assurance Testing'
login_page_url = 'http://52.39.5.126/login/index.php'
login_page_title = 'Software Quality Assurance Testing: Log in to the site'

# actual values
actual_app_url = 'http://52.39.5.126/'
actual_home_page_title = 'Software Quality Assurance Testing'
actual_login_page_url = 'http://52.39.5.126/login/index.php'
actual_login_page_title = 'Software Quality Assurance Testing: Log in to the site'


print(f'Launch {app} and go to to {app_url}')

if app_url == actual_app_url and home_page_title == actual_home_page_title:
    print(f'{app} is launched, home page is displayed')
    print(f'Go to Login Page')
    if login_page_url == actual_login_page_url and login_page_title == actual_login_page_title:
        print(f'{app} Login Page is displayed we can now login')
    else:
        print(f'{app} Login Page is not diplayed! Check your code!')
else:
    print(f'{app} Home Page is not diplayed! Check your code!')
