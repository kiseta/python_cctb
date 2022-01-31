__author__ = 'tk'
# The FOR LOOP in Python is used to iterate over a sequence (list, tuple, string) and
# other objects.

# 1. Print individual letters of a string using the FOR LOOP
word = 'Apple'
for letter in word:
    print(letter)

word2 = input('Enter any word: ')
for l in word2:
    print(l)

# 2. Using the FOR LOOP to iterate over a Python list or tuple
fruits = ['Apple', 'Banana', 'Cherry', 'Raspberry', 'Plum']
for f in fruits:
    print(f)
#
# 3. Program to find the sum of all int numbers stored in a list
# List of numbers
list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# create a var to store the sum
summary = 0

# iterate over the list of numbers
for value in list_of_numbers:
    summary = summary + value

print(f'The summary is {summary}')


# 4. Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']

# Iterate over the list using index
for i in range(len(genre)):
    print(f'I like', genre[i])
    print(f'I like {genre[i]}')

# 5. We can use for loop with else statement
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print('No items in the list.')

# 6. Program to display students' marks from journal
student_name = input('Enter name of the student: ')

# Let's make marks dictionary
marks = {'James': 90, 'Julie': 55, 'Brandon': 77}

for student in marks:
    if student == student_name:
        print(marks[student])

# PYTHON WHILE LOOP
# The WHILE LOOP in Python is used to iterate over the block of code
# as long as test expression (or condition) is TRUE.

# 1.Simple program to start at 1 and stop around 100
number = 1
step = 5    # You can specify the step
while number < 100:  # while number is True
    number += 1
    print(number)

# 2. Program to add numbers up to ...
# Take a number from user
n = int(input('Enter a number: '))

# Initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1

print(f'This is our sum {sum}')

# 3. Make a counter program using WHILE LOOP
counter = 1
step = int(input('Enter numbers of iterations: '))

while counter <= step:
    print(f'This is inside loop. Iteration # {counter}')
    counter = counter + 1
else:
    print(f'Loop finished. This is ELSE Statement')

# 4. Nested For Loop in Python
list_of_fruits = ['banana', 'mango', 'strawberry', 'nectarine']
for num1 in list_of_fruits:
    for num2 in range(14):
        print(f'{num1} {num2}')

# Using for loop print index : value pairs from a list or tuple
tropical_tuple = ('Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee')

for i in range(len(tropical_tuple)):
    print(f'{i} : {tropical_tuple[i]}')

# Using for loop print index : value pairs from a list or tuple
tropical_list = ['Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee']

for i in range(len(tropical_list)):
    print(f'{i} : {tropical_list[i]}')