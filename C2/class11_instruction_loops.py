__author__ = 'tk'

#  The FOR LOOP in Python is used to iterate over a sequence (list, tuple, string) and
#  other objects

# 1. Pring individual letter of a string using the FOR LOOP

word = 'Apple'
for letter in word:
    print(letter)

word2 = input('Enter a word: ')
for l in word2:
        print(l)

# Using the FOR LOOP to iterate over Python list or Tuple

fruits = ['Apple', 'Pear', 'Cherry', 'Plum', 'Mango']
for f in fruits:
    print(f)

for i in range(len(fruits)):
    print(f'{i} {fruits[i]}')

# Using for loop print index : value pairs from a list or tuple
tropical_tuple = ('Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee')

for i in range(len(tropical_tuple)):
    print(f'{i} : {tropical_tuple[i]}')

# Using for loop print index : value pairs from a list or tuple
tropical_list = ['Durian', 'Mangosteen', 'Jackfruit', 'Cherimoya', 'Lychee']

for i in range(len(tropical_list)):
    print(f'{i} : {tropical_list[i]}')


# 3. Program to find the sum of all int numbers stored in a list

list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# create a vaiable to store the sum
sum = 0

# iterate over the list of number
for value in list_of_numbers:
    sum = sum + value

print(f'The sum is {sum}')

# 4. Program to iterate through the list using indexing

genre = ['pop', 'rock', 'jazz'] # list

# Iterate over the list using index
for i in range(len(genre)):
    print(f'I like', genre[i])
    print(f'I like {genre[i]}')
    print(f'I like %s' % genre[i])

# 5. We can use for loop with else statement
digits = [0, 1, 5] #list
for i in digits:
    print(i)
else:
    print('End of the list.')

# 6. Program to displays student marks from journal
student_name = 'Ellen' #input('Enter a student name: ')

# Let's make marks dictionary
marks = {
    'James': 90,
    'Julie': 55,
    'Brandon': 77
}
count = len(marks)
for student in marks:
    if student == student_name:
        print(marks[student])
    else:
        print(f' Student {student_name} was not found')
else:
    print(f'End the loop')

# PYTHON WHILE LOOP
# The WHILE LOOP IN PYTHON is used to iterate over the blok of code
# as long as test expression (or condition) is true

num = 10
var = 10
while num: # while number is True
    var = var + 1
    print(f'Var: {var}')


while num != 0: # while number is True
    var = var + 1
    num -= 1
    print(f'Var: {var}')
    print(f'Num: {num}')

# 1. Simple program to start at 1 and stop at 100
num = 1
step = 3 # how much to add each step
while num < 100: # while number is True
    num += step
    print(num)

# 2. Program to add numbers up to ...
# Take a number from user
n = int(input('Enter a number: '))

# initialize total and counter
sum = 0
i = 1

while i <= n:
    #sum += i
    sum = sum + i
    i = i + 1

print(f'This is our sum {sum}')

# 3. Make a counter program using WHILE LOOP
counter = 0
step = int(input('Enter number iterations: '))

while counter <= step:
    print(f'This is inside loop. Iteration # %s' % counter)
    counter = counter + 1
else: print(f'Done ✔')

# 4. Nested For Loop in Python

for num1 in range(3):
    for num2 in range(10, 14):
        print(f'{num1} {num2}')
        print('%s %s' % (num1, num2))