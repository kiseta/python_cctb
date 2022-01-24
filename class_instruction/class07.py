__author__ = 'tk'

# Python programming language introduction CLASS 1
# comments in Python preceede with # character
# to comment select your code and press Ctrl? or Ctrl/

# printing values
# print('I love green smoothie!')
# print("It's really good!")

# string variable type
# name = "awesome students"
# print ("Hello " + name)
# print(type(name))

# concatinating strings
# first_name = "awesome"
# last_name = "students"
# full_name = first_name + " " + last_name
# print ("Hello " + full_name)

# integer variable type
# age = 21
# age = age + 1
# age += 1
# print(type(age))
# print("Your age is: " + str(age))
# print(str())

# float variable type
# height = 250.5
# print(height)
# print(type(height))
# print("Your height is: " + str(height) + "cm")

#boolean
#human = True
#print("Are you human? " + str(human))

#multiple assignments
# fname, lname, age = "John", "Smith", "25"
# print(fname)
# print(lname)
# print(age)
# print(fname + " " + lname + " " + age)
# var1 = var2 = var3 = 30
# print(var1)
# print(var2)
# print(var3)

#useful string functions
# name = "automation Class"
# number = " 456 "
#print(len(name))
#print(name.find("d"))
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
# x = float(x)
# y = float(y)
# z = float(z)
#
# # type cast (convert) to string
# x = str(x)
# y = str(y)
# z = str(z)
#
# print(x)
# print(y)
# print(z*3)

# input values
name = input("What is your name?: ")
print(name)
# activity = input("What are you doing?: ")
# print(activity)
age = int(input("How old are you?: ")) #convert sting (input is always string) to integer for further calcuations
age = age + 1
print("You are " + str(age) + " years old") #convert interger to string for string cancatination

height = float(input("How tall are you?: "))
print("You are "+ str(height) + "cm tall")