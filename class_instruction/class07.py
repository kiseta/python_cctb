__author__ = 'tk'

# Python programming language introduction CLASS 1
# comments in Python preceede with # character
# to comment select your code and press Ctrl? or Ctrl/

# printing values
print('Hello, Team!') # printing strings
print('Welcome to Class!')
print(2022) # printing integers
print(24)
print('We are open', 7, 'days a week.') # printing combination of strings and integers

# concatenating strings
first_name = "awesome"
last_name = "students"
full_name = first_name + " " + last_name
print ("Hello", full_name)


# Now let's talk more about variables and variable types

# VARIABLE TYPE - STRING

# string variable type
n = "awesome students"
print ("Hello " + n)
print ("Hello", n)
print(type(n)) # useful built-in function type() - returns variable type

# integer variable type - whole numbers without a decimal point
age = 21
age = age + 1 # legacy
age += 1 # modern
print(type(age))  # useful built-in function type() - returns variable type
print("Your age is: " + str(age))
print("Your age is:", age)
print(str())

# float variable type - floating point numbers with decimals
height = 115.7
print(height)
print(type(height))
print("The tallest tree is : " + str(height) + "meters tall")
print("The tallest tree is:", height, "meters tall")

#boolean
yes = True
no = False
print("Are you human? " + str(yes))
print('Are you robot?', no)
print('Is D2R2 human? %s' % no)
print(f'Is D2R2 robot? {yes}')

# USEFUL OPERATIONS WITH VARIABLES IN PYTHON
#multiple assignments
# fname, lname, age = "John", "Smith", "25"
# print(fname)
# print(lname)
# print(age)
# print(fname + " " + lname + " " + age)
# print(fname, lname, age)
# var1 = var2 = var3 = 30 # when you need to assign the same value to 3 different variables
# print(var1)
# print(var2)
# print(var3)

#useful string functions
# name = "The Ultimate Answer to Life "
# number = " 42 "
#print(len(name))
#print(name.find("t"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
#print(name.isdigit())
#print(number.isdigit())

# print(name.isalpha())
# print(number.isalpha())
# print(name.count("t"))
# print(number.replace(" ", ""))
# print(name*3)


# type casting = changing variable type
x = 1 #integer
y= 2.0 #float
z= "3" #string

# #type cast (convert) to float type
x = float(x)
y = float(y)
z = float(z)
#
# # type cast (convert) to string
x = str(x)
y = str(y)
z = str(z)

print(x)
print(y)
print(z*3)

# input values from the user
name = 'Edward'
print('Hello', name)
activity = 'playing piano'
print('You are very good at', activity)
birth_year = 1901
print("You are now " + str(2022 - birth_year) + " years old")
height = 198
print("You are "+ str(height) + " cm tall")

# input values
# name = input("What is your name?: ")
# print('Hello', name)
# activity = input("What are you doing?: ")
# print('You are very good at', activity)
# birth_year = int(input("Year you were born?: ")) #convert sting (input is always string) to integer for further calcuations
# age = 2022 - birth_year
# print("You are now " + str(age) + " years old") #convert interger to string for string cancatination
# height = float(input("How tall are you?: "))
# print("You are "+ str(height) + " cm tall")