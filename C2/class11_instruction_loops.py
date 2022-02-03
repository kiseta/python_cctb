__author__ = 'tk'

#  The FOR LOOP in Python is used to iterate over a sequence (list, tuple, string) and
#  other objects

# 1. Print individual letter of a string using the FOR LOOP

word = 'Python'
for letter in word:
    print(letter)

word2 = input('Enter a word: ')
for l in word2:
        print(l)

# Using the FOR LOOP to iterate over Python list or Tuple

music_genres = ['Electronic', 'Jazz', 'Oldies', 'Classical', 'Blues']
for f in music_genres:
    print(f)

# Using for loop print index : value pairs from a list or tuple
music_tuple = ('Electronic', 'Jazz', 'Oldies', 'Classical', 'Blues')

for i in range(len(music_tuple)):
    print(f'{i} : {music_tuple[i]}')

# Using for loop print index : value pairs from a list or tuple

tropical_list = ['Durian', 'Mango', 'Jackfruit', 'Cherimoya', 'Lychee']

for i in range(len(tropical_list)):
    print(f'{i} : {tropical_list[i]}')


# 3. Program to find the sum of all int numbers stored in a lit

list_of_numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# create a vaiable to store the sum
sum = 0

# iterate over the list of number
for value in list_of_numbers:
    sum = sum + value

print(f'The sum is {sum}')

# 4. Program to iterate through the list using indexing

genre = ['chill', 'oldies', 'jazz'] #list

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
grades = {
    'James': 90,
    'Julie': 55,
    'Brandon': 77
}
count = len(grades)
for student in grades:
    if student == student_name:
        print(grades[student])
    else:
        print(f' Student {student_name} was not found')
else:
    print(f'End the loop')

# PYTHON WHILE LOOP
# The WHILE LOOP IN PYTHON is used to iterate over the blok of code
# as long as test expression (or condition) is true

number = 10
var = 10
while number: # while number is True
    var = var + 1
    print(var)

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


# 5.Program to check the number from the given range
# Program requirements
# Check if entry is an intteger
# Check if the entry is in range
# Keep prompting to enter a number until the correct value is entered

numbers = None
valid_flag = False
while not valid_flag:
    try:
        numbers = int(input('Please enter any integer number from 1 to 10: '))
        while 0 < numbers <= 10:
            print(f'All good. Your number {numbers} is from 1 to 10.')
            valid_flag = True
            break
        else:
            print(f'Your number {numbers} is not from a given range. Please try again!')
    except ValueError as e:
        print(f'You entered non integer value. Please try again! Error message: ', e)
    finally:
        print('The program is done!')