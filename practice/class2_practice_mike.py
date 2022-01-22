# Displaying strings
print('Hello World')  # Display Hello World
print('Today is a wonderful day ever!')  # Display cool message
print('Hey my dear team!')  # Display message about my team
print('My temperature now is 37.5')  # Display my current body's temperature
print('Cool! Very nice!')  # Display just very cool message

# Display integers
print(38)  # Display my age
print(2022)  # Display current year
print(2021)  # Display previous year
print(1983)  # Display my YOB
print(2013)  # Display my year - landed in Canada

# Combined display of numbers and text
print('I have', 2 * 2, 'apples')

print('My age' + str(2))

age = 38
year = 2022
college_name = 'CCTB'
class_started = True
class_duration = 45.0

# Formatting strings
print(f'My age {age} and I am happy. Now is {year} year')

# Class duration
print(f'Hi, my name is Mike, I am {age} years old. Now is {year} year and I am working as Instructor at {college_name} \
. Class duration is {class_duration} minutes. If class already started, tell me {class_started}.')

print('Hi, my name is Mike, I am ' + str(age) + ' years old. Now is ' + str(year) + ' year and I am working as '
                                                'Instructor at ' + college_name + ' . Class duration is ' + str(
    class_duration) + 'minutes. If class already started, tell me ' \
      + str(class_started) + '.')

# Concatenation
# print('My age  + str(age) + ' + 'and I am happy. Now is' + str(year) + ' year')

print('#################################')
print('I have', 2, 'apples', '!', True, 29.50)

# Practice with different data types
print('657467647764')

# TASK 1
# DISPLAY ANY 5 STRINGS, ANY 5 INTEGERS, ANY 5 FLOATS and 2 BOLLEANS
print('Welcome to', 'Canada', '. This country is so beautiful. Canada became a country in', 1867, '\
as the Dominion of Canada. This is', True, 'that British Columbia is Canada\'s westernmost province. '
                                           'BC has population of', 5, 'million people. The City of Vancouver has',
      'population of', 2.600, 'million people. There was a', False, 'alarm today in a morning. '
                                                                    'Riddle. I had', 5, 'apples.', 2,
      'apples I gave to Tatyana.', 1, 'apple was given to Jason. How many apples Mike has? '
                                      'Correct answer is not', 4, 'and not', 7, 'right?', 'Also not', 2.5,
      'apples and not', 78.45654, ', are you agree?', 'Class will be done in', 45, 'minutes')

# TASK 2
# DISPLAY THEN USING f'' formatting strings functionality in one print shot. 17 values in total.
# YOU CAN ALSO USE ANY ADDITIONAL STRINGS TO ENHANCE STRINGS MEANING

# STRINGS: ANY VALUES INSIDE QUOTES, EVEN NUMBERS, BOOLS, FLOATS
# 'Hello', '657467647764'

# INTEGERS: ANY WHOLE NUMBERS W/O DECIMAL POINT AND NOT INSIDE QUOTES
# 0, -45, -1000000000000000000000000

# FLOATS: ANY NUMBERS (POS or NEG) WITH DECIMAL POINT
# -1000000000000000000000000.0

# BOOLEANS: TWO VALUES ONLY - TRUE or FALSE
# False, True

# name = input('Enter your name: ')
# age = int(input('Enter your age: ')) # BY DEFAULT INPUT CONVERTS ANY VALUES INTO STRINGS
# college = input('Enter name of the college: ')
# print('Hello World, my name is %s and I am %s years old. I\'ve been working at %s' % (name, age*2, college))

# Declare 5 vars
# Assign them an input values
# Display them using %s string formatter in one line using print() command
# Please use different data types (int and str)

country_name = input('Enter country name: ')
province_name = input('Enter province name: ')
city_name = input('Enter your city name: ')
house_number = int(input('Enter your house number: '))
address = input('Enter your address: ')

print('Hey! I live in %s and in %s in the City of %s. My address is '
      '%s %s' % (country_name, province_name, city_name, house_number, address))