

fruits = ['Apple', 'Pear', 'Cherry', 'Plum', 'Mango']

for f in fruits:
    print(f)

for i in range(len(fruits)):
    print(fruits[i])

num = 10
var = 10
# while num != 0: # while number is True
#     var = var + 1
#     num -= 1
#     print(f'Var: {var}')
#     print(f'Num: {num}')

# infinite print
while num: # while number is True
    var = var + 1
    num -= 1
    print(f'Var: {var}')
    print(f'Num: {num}')