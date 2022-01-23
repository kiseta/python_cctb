__author__ = 'tk'

# Lab 9 - Tatyana
# Do the following tasks.
# 1. Create a new program in PyCharm where you will check the current weather and display funny messages based on your input.
# 2. If the user will enter integer values more than 0 but less than 15 degrees, display a message to wear something related to that weather condition.
# 3. If the user will enter integer values more than 15 but less than 35 degrees, display a message to wear something related to that weather conditions.
# 4. If the user will enter integer values more than 35 degrees, display a message to wear something related to that weather conditions.
# 5. If the user will enter integer values less than 0 degrees, display a message to wear something related to that weather conditions.

temp = int(input('Please enter today\'s temperature in Celcius: '))

if temp >= 0 and temp < 15:
    print(f'{temp}°C - Not too cold! You still probably need a jacket!')
elif temp >= 15 and temp < 35:
    print(f'{temp}°C - Great! You can wear light clothes!')
elif temp >= 35 and temp < 59:
    print(f'{temp}°C - Nice and toasty! You can wear short shorts!')
elif temp < 0 and temp >= -89:
    print(f'{temp}°C - Brrr! Wear a hat and a scarf and don\'t forget your gloves')
else:
    print(f'{temp} - Hmm! Curious where you are, are you on Earth?')
