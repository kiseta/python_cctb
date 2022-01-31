# __author__ = 'tk'
# 1. Display any 5 strings in one line using the print() command
print('Hello, World!', 'It\'s a wonderful day', 'Python is awesome!', 'I\'m looking forward to the weekend', 'I hope I can still go skiing')
# 2. Display any 5 integers in one line using the print() command
print(365, 12, 7, 24, 8)
#
# 3. Display any 5 float numbers in one line using the print() command
print(3.14159, 36.6, 8.5, 0.5, -0.99)

# 3. Display a combination of integers and strings in one line
print('In',2014, 'a talented singer Angelina Jordan won the', 1, 'st place in a TV Show \'Norway Got Talent\' when she was just', 5, 'years old.')

# 4. Define a few variables and give an example on how to use f'' formatting strings (display strings and numeric variables)
year = 2014
name = 'Angelina Jordan'
place = 1
show = '\'Norway Got Talent\''
age = 5
print("1-In " + str(year) + ", a talented singer " + name + ", won the " + str(place) + "st place in a TV Show " + show + ", when she was just " + str(age) + " years old.")
print('2-In',year, 'a talented singer', name, 'won the', place, 'st place in a TV Show', show, 'when she was just', age, 'years old.')
print(f'3-In {year}, a talented singer {name}, won the {place}st place in a TV Show {show}, when she was just {age} years old.') # <-- shortest
print("4-In %s, a talented singer %s, won the %sst place in a TV Show %s, when she was just %s years old." % (year, name, place, show, age))


#
# 5. Display in one print command 5 strings, 5 integers, 5 float numbers and 2 boolean values together
print('Earth is the only planet in Solar system with just', 1, 'Moon!',
      '\nWhat planet in Solar system has the most moons?', '\nIs it Saturn?', True, 'Saturn has', 83, 'moons.',
      '\nIs it Jupiter?', False, 'Jupiter has', 79, 'moons.', '\nBoth Mercury and Venus have', 0, 'moons.')

# 6. Combine print and input together in one line
print('Your answer is: '+ input('Do you believe in magic?: '))

# 7. Provide multiple inputs in one go
i, j, k = input('Quickly enter three colors separated by space: ').split()
print('Your favorite colors are: '+ i, j, k)
#
# 8. Reversing a string in Python
name = input('Enter your favorite movie title: ')
print("Here is your favorite movie title in Reverse: ", name[::-1])
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
trk_num = conf_msg_split[-1] # capture the last item
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
first_name = "Edward"
lastname = "Cullen"

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