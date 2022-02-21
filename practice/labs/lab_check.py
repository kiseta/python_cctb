# 1. Create a new program in PyCharm where you will check the current weather and display funny messages based on user input.

# 2. If the user enters integer values more than 0 but less than 15 degrees, display a message to wear something related to that weather condition.

# 3. If the user enters integer values more than 15 but less than 35 degrees, display a message to wear something related to that weather condition.

# 4. If the user enters integer values more than 35 degrees, display a message to wear something related to that weather condition.

# 5. If the user enters integer values less than 0 degrees, display a message to wear something related to that weather condition.

print(f'Welcome to weather Podcasts! we explore the various ways weather and its impacts our lives.')
tweather = int(input('Please enter todays weather: '))
if tweather > 0 and tweather <= 15:
    print(f'Todays weather is {tweather} degree. Not bad! You can enjoy the clouds and chilly winds')
elif tweather > 15 and tweather <= 35:
    print(f'Todays weather is {tweather} degree. Hurry! Summar is here enjoy the Sunny day')
elif tweather > 35:
    print(f'Todays weather is {tweather}. Warning signs! Stay at home, keep hydrated')
elif tweather < 0:
    print('Its Snow time!! December is here time to celebrate New year')
else:
    print(f'something went wrong please enter correct value: {tweather}')
