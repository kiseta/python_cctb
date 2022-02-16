# CONDITIONAL STATEMENTS

# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y


# COMPARISSON OPERATORS TABLE
# < LESS THAN
print(3 < 5)
print(3 > 5)

# LESS THAN OR EQUAL
print(6 <= 9)

# > GREATER THAN
print(10 > 2)
print(10 < 2)

# GRATER THAN OR EQUAL
print(24 >= 23)

# EQUAL ==
print (5 == 5)

# not equal !=
print (5 != 5)
print (5 != 6)

# checking string values
expected_title = "CCTB - Welcome!"
actual_title = "404 - Page Not found"

print(expected_title == actual_title)
print(expected_title != actual_title)

print('--------------- test negaitive ---------------------------')
expected_title = "CCTB - Welcome!"
actual_title = "404 - Page Not found"

if expected_title == actual_title:
    print('CCTB Website is launched')
else:
    print('Website is down. Contact your system administrator')

print('--------------- test positive ---------------------------')
expected_title = "CCTB - Welcome!"
actual_title = "CCTB - Welcome!"

if expected_title == actual_title:
    print('CCTB Website is launched')
else:
    print('Website is down. Contact your system administrator')


# program to check the age
age = 15
your_age = int(input('Please enter your age: '))

if age >= your_age:
    print(f'Your age {your_age} is less than or equal {age}')

elif age <= your_age:
    print(f'Your age {your_age} is grater than or equal {age}')

else:
    print(f'We don\'t know what your age is please try again!')


# IF, ELIF, ELSE syntax - pay attention to spacing and indentation

# if [condition]:
    # code to execute if the statment is true
# elif [condition]:
    # code to execute if the statement is true
# elif [condition]:
    # can have multiple elif statements
# else:
    # code to execute for any other situation

# indent - Tab
# unindent - Shift + Tab

# conditional statements practice

# program that check for a user age
# we are at the games website
# our program recommend games based on user age

print(f'Welcome to our website! We can help you pick the right game for your age.')
age = int(input('Please enter your age: '))

if age > 20 and age <= 40:
    print(f'Your age is {age}. Not bad! You can play the following games: G1, G2, G3')
elif age > 11 and age <= 20:
    print(f'Your age is {age}. Cool! We suggest these games for you: G4, G5, G6')
elif age > 5 and age <= 10:
    print(f'Your age is {age}. Awesome! Let\'s play these games: G7, G8, G9')
elif age == 0:
    print('You\'re not born yet. Please wait for a few years!')
else:
    print(f'We don\'t have any games for your age: {age}')

# program that check the nationality and greets the user in their language
nationality = input('What is your nationality? Type: English, Russian, Indian, Chinese, Filipino, Macedonian, Arabic, Persian, Bangla: ')

age = int(input('Enter your age: '))

if nationality == 'english' and age < 15:
    print('I\'m gonna say Heyyyaaa to you')
elif nationality == 'english' and age > 15:
    print('I\'m gonna say Hello to you')
elif nationality == 'Russian':
    print('I am going to say Privet‚ to you!')
elif nationality == 'Indian':
    print('I am going to say Namaste to you!')
elif nationality == 'Chinese':
    print('I am going to say Ni Hao to you!')
elif nationality == 'Filipino':
    print('I am going to say Salamat to you!')
elif nationality == 'Macedonian':
    print('I am going to say Zdravo to you!')
elif nationality == 'Arabic':
    print('I am going to say Marhaba to you!')
elif nationality == 'Persian' or nationality == 'Bangla':
    print('I am going to say Salam to you!')
else:
    print(f'Sorry we don\'t know your nationality: {nationality} but Hi to you anyway!')

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

# 15% on the first $50,197 of taxable income, plus
# 20.5% on the next $50,195 of taxable income (on the portion of taxable income over 50,197 up to $100,392), plus
# 26% on the next $55,233 of taxable income (on the portion of taxable income over $100,392 up to $155,625), plus
# 29% on the next $66,083 of taxable income (on the portion of taxable income over 155,625 up to $221,708), plus
# 33% of taxable income over $221,708

amount = int(input('Please enter annual income amount: '))

if amount <= 50197:
    tax = (amount * .15)
    netpay = amount - tax
    print(f'Amount: {amount}\nTax: {tax}\nNetPay: {netpay}')
elif amount > 50197 and amount <= 100392:
    tax = (50197 * .15) + ((amount - 50197) * .205)
    netpay = amount - tax
    print(f'Amount: {amount}\nTax: {tax}\nNetPay: {netpay}')
elif amount > 100392 and amount <= 155625:
    tax = (50197 * .15) + (50197 * .205) + ((amount - 50197 - 50197) * .26)
    netpay = amount - tax
    print(f'Amount: {amount}\nTax: {tax}\nNetPay: {netpay}')
elif amount > 155625 and amount <= 221708:
    tax = (50197 * .15) + (50197 * .205) + (55233 * .205) + (66083 * .26) + ((amount - 50197 - 50197 - 55233) * .26)
    netpay = amount - tax
    print(f'Amount: {amount}\nTax: {tax}\nNetPay: {netpay}')
