def calc(a, b, sign):
    if sign == '+':
        print(f'The result of addition {a + b}')
    elif sign == '-':
        print(f'The result of substrcation {a - b}')
    elif sign == '*':
        print(f'The result of multiplication {a * b}')
    elif sign == '/':
        print(f'The result of float division {a / b}')
    elif sign == '//':
        print(f'The result of interger division {a // b}')
    else:
        print(f'Something is wrong. Please check your arguments {a, b, sign}')

# Addition
calc(5, 5, input(f'Enter sign operator: '))
# Subtraction
calc(5, 5, input(f'Enter sign operator: '))
# Multiplication
calc(5, 5, input(f'Enter sign operator: '))
# Division
calc(5, 5, input(f'Enter sign operator: '))
# Division
calc(5, 5, input(f'Enter sign operator: '))

def find_between_r(val, first):
    try:
        start = val.find(first) + len(first)
        end = len(val)
        return val[start:end]
    except ValueError:
        return ""

print(find_between_r('http://52.39.5.126/user/view.php?id=5363','='))