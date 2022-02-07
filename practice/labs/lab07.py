__author__ = 'tk'
# 1. Display any 5 strings in one line using the print() command

print("Hello", "My name is Tatyana,", "I came to Canada in 2004,", "I am a Test Automation Engineer,",
      "I currently work at CCTB teaching Test Automation")

print(
    'How to make a delicious %s! Add to the %s: %s, %s, and %s. Blend until smooth. Pour into a fancy glass and enjoy!' % (
    'Green Smoothie', 'High Speed Blender', '2 Bananas', '2 cups Pineapple', '2 cups Spinach'))

# 2. Display any 5 integers in one line using the print() command
print('The Moons\'s diameter is ' + str(3475) + ' km and the distance from Earth is ' + str(
    384400) + ' km. The Sun\' diameter is ' + str(1392530) + ' km, and the distance from Earth is ' + str(
    149597870) + ' km')
print(
    "The reason we get to enjoy eclipses is because the ratio of diameter to distance for the Moon and "
    "the Sun is practically identical, with the Sun\'s being slightly bigger")

# 3. Display any 5 float numbers in one line using the print() command

print('The most famous floating point numbers are pi:',3.14159274, 'Human body temperature: ', 36.6, 'Although anything within the range of', 36.1, 'to', 37.2,' can be a healthy, normal human temperature')
sun_dm = 1392530
sun_ds = 149597870
sun_ds_to_dm = (sun_dm / sun_ds)*100

moon_dm = 3475
moon_ds = 384400
moon_ds_to_dm = (moon_dm / moon_ds)*100

print('Sun\'s diameter to distance from Earth ratio: ' + '%.2f' % sun_ds_to_dm)  # format to display 2 decimals
print('Moons\'s diameter to distance from Earth ratio: ' + '%.2f' % moon_ds_to_dm)  # format to display 2 decimals

# 3. Display a combination of integers and strings in one line
year = 2014
name = 'Angelina Jordan'
place = 1
show = '\'Norway Got Talent\''
age = 5

# In 2014, a young singer Angelina Jordan, won the 1st place in a TV Show 'Norway Got Talent', when she was just 5 years old.
print("1-In " + str(year) + ", a young singer " + name + ", won the " + str(place) + "st place in a TV Show " + show + ", when she was just " + str(age) + " years old.")
print('2-In',year, 'a young singer', name, 'won the', place, 'st place in a TV Show', show, 'when she was just', age, 'years old.')
print(f'3-In {year}, a young singer {name}, won the {place}st place in a TV Show {show}, when she was just {age} years old.') # <-- shortest
print("4-In %s, a young singer %s, won the %sst place in a TV Show %s, when she was just %s years old." % (year, name, place, show, age))


# 4. Define a few variables and give an example on how to use f'' formatting strings (display strings and numeric variables)
days_year = 365
human_years = 100
hours_day = 24
human_days = days_year * human_years
human_hours = human_days * hours_day
conclusion = 'That does not seem like a lot so don\'t waste it!'
print(
    f'There are {days_year} days in a year and approximately {human_years} years in human life, so there are about {human_days} days \n'
    f' and about {human_hours} hours in human life. {conclusion}')

# 5. Display in one print command 5 strings, 5 integers, 5 float numbers and 2 boolean values together

print('Earth is the only planet in Solar system with just ', 1, 'Moon', '!','What planet in Solar system has the most moons?', 'Is it Saturn?', True, 83, 'Is it Jupiter?', False, 79)

# 6. Combine print and input together in one line
print('Your answer is: '+ input('Do you believe in magic? Enter yes or no: '))

# 7. Provide multiple inputs in one go
i, j, k = input('Quickly enter three colors separated by space: ').split()
print('Your favorite colors are: '+ i, j, k)

# 8. Reversing a string in Python
name = input('Enter your favorite movie title: ')
print("Here is your favorite movie title in Reverse: ", name[::-1].lower().capitalize())

# 9. In-Place Swapping Of Two Numbers
a, b = 100, 200

print('a is: ', a)
print('b is: ', b)
a, b = b, a
print('reverse a is: ', a)
print('reverse b is: ', b)

# 10. Check The Memory Usage Of the Variable

import sys
m = "Mars is the fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury. \n" \
    "In English, Mars carries the name of the Roman god of war and is often referred to as the \'Red Planet\'."
print(m)
print('Memory Usage in bytes: ', sys.getsizeof(m)) # Return the size of object in bytes

# 11. Print string N times
sing = "Let It Snow! "
n = 3
print(f'Sing it {n} times:', sing*n)

# 12. Splitting a string into a list
conf_msg = 'Thank you for your order. Your tracking number is TR239402983'
conf_msg_split = conf_msg.split()
print(conf_msg_split)
print(len(conf_msg_split))
trk_num = conf_msg_split[-1]
print(trk_num)

# 13. Display multiple input values in a single line

name, quantity, unit = input('Enter fruit name, color, and quantity info separated by space: ').split()
print('Ingredient Name: ', name)
print('Ingredient Color: ', quantity)
print('Ingredient Quantity: ', unit)

# 14. Give 3 incorrect names of the variables
# start with number
#100years = 100

# special characters in variable names, anything in Shift+1-0, '_' underscore is ok
# $amount = 10

# non-latin alphabet chars, some will work but not everywhere and not a common practice
# адрес = "123 Main st."
# print(адрес)

# 15. Give 3 correct names of the variables
i = 1
count = 3
first_name = "Sam"
lastName = "Carter"

# 16. What is the purpose of using variables?
# Variables are used to store data values

# 17. How can we define a constant variables? Give an example.

HOURS_IN_A_DAY = 24  # unless  you are on Mars then it's 25
print('There are', HOURS_IN_A_DAY, 'hours in a day on Planet Earth')
print('unless you are on Mars, then it\'s', HOURS_IN_A_DAY + 1, 'hours in a day')

# 18. What reserved Python keywords we can't use to define a variables? Provide as much as you can.
# Variable names cannot be used if they already reserved by Python.
# int, str, bool, float, for, while, break, continue, try, except, finally, True, False, if, elif, else, and, or
# Variable names cannot be used as Python built-in functions
# https://docs.python.org/3/library/functions.html

