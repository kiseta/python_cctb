__author__ = 'tk'

# Comments in Python language are line of text preceeded with the #
# if you want comments on
# multiple lines
# select code and press Ctrl (Windows) Cmd (Mac) +? (plus question mark on the keyboard)

# display Hello, World string
print('Hello, World!')

# Lets practice printing strings
print('Python is awesome')
print('The Page is loaded')
print('Hello', 'World', '!' )

# print today's year
today_year = 2022
print(today_year)
print('2022')

# print string and a number together
print('Today\'s Year: '+ str(2022)) # concatenation requires variable type conversion to str
print('Today\'s Year:', 2022)
print('Days in a week: ' + str(7))
print('Days in a week:', 7)

# printing combination of strings and integers in one line
print('I came to Canada in', 2004, 'Now it is year', 2022,'. So I\'ve been in Canada for', 18, 'years' )


# Printing methods in Python

c = 'Thank you for buying with Advantage!' # string
tn = 3220482580 # interger
on = 3220511624 # integer

# Method 1
# Printing with concatenation
print('Method 1: ' + c + ' Your tracking number is ' + str(tn) + '. Your order number is ' + str(on))

# Printing values separated by commas
print('Method 2:', c, 'Your tracking number is', tn, '. Your order number is', on)

# printing with formatting strings method
print(f'Method 3: {c} Your tracking number is {tn}. Your order number is {on}')

# Printing with %s formating
print('Method 4: %s Your tracking number is %s. Your order number is %s' % (c, tn, on))


print('Hello, Team!') # pring string value
print(2022) # print number
print('We are open ' + str(7) + ' days a week')  # legacy
print('We are open', 7, 'days a week.') # modern way to print in Pyton
n = 7
print(f'We are open {n} days a week')
print('We are open %s days a week' % n)

s = 'Hello, Team!' # string type
i = 24 # integer type - whole numbers without decimal point

# float variable - floating point numbers with decimal point
pi = 3.14159
ht = 36.6

# boolean type True False
yes = True
no = False
print('Are you human? ' + str(True) )
print('Are you robot?', False)

age = 21 # created a variable
newage = age + 1
newage = float(newage)
print('My sister\'s age is: ', newage)

# use type() built in Python function to find variable type
print(type(newage))
print(type(s))
print(type(yes))
print(type(pi))
print(type(i))

print(s * 2) # using multiplication with the string will print it 2 times
print(i * 2)



# Useful operations with variables in Python

# multiple assignments
fname, lname, emaladdress = 'John', 'Smith', 'js@yahoo.com'
print(fname)
print(lname)
print(emaladdress)

# assign the same value to 3 different variables
price1 = price2 = price3 = 50
print(price1 / 2)
print(price2 * 2)
print(price3 + price1 + price2)

# useful string function
name = 'The Ultimate Answer to Life'
number = " 42 "

# determine the length of name variable value - len()
print('Count of characters: ', len(name))
print(name.find('T')) # case sensitive find('t') is different from find('T')
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalpha())
print(name.isdigit())
print(number.isdigit())

print(name.lower().count('t'))
print(len(number))
number = number.replace(" ", "")
print(number)
print(len(number))

# TYPE CASTING IN PYTHON - CONVERTING VARIABLE TYPES
# type casting in Python is converting one variable type to another

x = 1 # integer
y = 2.0 # float
z = "3" # string

x = float(x) # convert interger to float
print(x)
y = int(y) # convert float to integers
print(y)
z = float(z) # convert string to float
print(z)
print(z * 2)

x = str(x) # convert integer to string
y = str(y) # convert float to string
z = str(z) # convert float to string
