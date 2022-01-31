# Comments in Python language are line of text preceeded with the #
# if you want comments on
# multiple lines
# you select code and press Ctrl (Windows) Cmd (Mac) +?

# display Hello, World string
# print('Hello, World!')
#
# # Lets practice printing strings
# print('Python is awesome')
# print('The Page is loaded')
# print('Hello', 'World', '!' )
#
# # print today's year
# today_year = 2022
# print(today_year)
# print('2022')
#
# # print string and a number together
# print('Today\'s Year: '+ str(2022)) # concatenation requires variable type conversion to str
# print('Today\'s Year:', 2022)
# print('Days in a week: ' + str(7))
# print('Days in a week:', 7)
#
# print('I came to Canada in', 2004, 'Now it is year', 2022,'. So I\'ve been in Canada for', 18, 'years' )


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



# print('I came to Canada in', 2004, 'Now it is year', 2022,'. So I\'ve been in Canada for', 18, 'years' )
