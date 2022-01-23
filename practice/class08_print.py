__author__ = 'tk'
# display Hello World string
# print("Hello, World!")
# print('Hello, World!')
# print("Python is awesome")
# print("Python is not named after the snake")
# print("It's lovely weather today in Vancouver")
# print("The snow has melted")
# print("And I still  haven't gone skiing!")
#
# # display my height as integer
# print("My height is: " + str(175)+ " cm") # print my height
# print("I came to Canada in " + str(2004)) # print the year I came to Canada
# print(2022) # print the year now
# print(7) # print the number of days in a week
# print(float(365)) # print the number of days in a year


# TASK 1
# DISPLAY ANY 5 STRINGS, ANY 5 INTEGERS, ANY 5 FLOATS and 2 BOLLEANS
# TASK 2
# DISPLAY THEN USING f'' formatting strings functionality in one print shot. 17 values in total.
# YOU CAN ALSO USE ANY ADDITIONAL STRINGS TO ENHANCE STRINGS MEANING

# start= "There are"
# prx = 'approximately'
# l = 'in human life'
# d = 'days'
# y = 'years'
# h = 'hours'
# dy= 365 # days in a year
# lsp = 100 # human lifer span
# dh= dy*lsp # days in human life
# hh = dh*24 # hours in human life
# hs = dh*8 # hours sleeping
# ah = hh-hs # hours awake
# sp = (hs/hh)*100 # sleep percentage
# yes = True
# no = False
#
# # print approximate number of days in a human life
# print("There are approximately " + str(dh) + " days in human life to play, have fun, and enjoy life")
# # print total hours vs hours sleeping
# print("There are approximately " + str(hh) + " hours in human life. We spend about " + str(hs) + " hours sleeping")
# print("That's about " + str(float(sp))+ " %")
#
# # ---------------------------------------------------------------
# # print using f'' - formatting
# print(f'{start} {dy} {d} in a {y}. {start} {prx} {hh} {h} in human life. We spend about {sp}% of it sleeping. Are you happy? {yes}! Are you sad? {no}. Can you play an instrument? {yes}! Is it piano? {no}.')
# # ---------------------------------------------------------------
#
# print("There are approximately %s hours in human life. We spend about %s hours sleeping" % (dh,hs))
#
# # combine display of numbers and text
# #print('I have', 2, 'apples', True, False, 345.45,'!@')
#
# daysYear = int(input("Enter the number of days in a Year: "))
# hoursDay = int(input("Enter the number of hours in a day: "))
# print("There are %s days in a year and %s hours in a day, so there are %s hours in a year" % (daysYear, hoursDay, daysYear*hoursDay))
# --------------------------------------------------------------------------
# recipe = input("What are we making?: ")
# ing = input("How many ingredients?: ")
#
# ing1 = input("Enter the first ingredient: ")
# q1 = input("Enter the first ingredient quantity: ")
# ing2 = input("Enter the second ingredient: ")
# q2 = input("Enter the second ingredient quantity: ")
# ing3 = input("Enter the third ingredient: ")
# q3 = input("Enter the third ingredient quantity: ")
# ing4 = input("Enter the fourth ingredient: ")
# q4 = input("Enter the fourth ingredient quantity: ")
# equip = input("Enter the equipment: ")
# print('How to make a delicious %s! Use the %s. Add %s %s, %s %s,  %s %s, %s %s and blend until smooth. Pour into a fancy glass and enjoy!' % (recipe, equip, q1,ing1, q2, ing2, q3, ing3, q4, ing4) )

# i = 1
# ingredient_count = input("How many ingredients?: ")
# ingredients = []
# while i <= ingredient_count:
#   ingredients = ingredients + (input("Enter ingredient " + i + " : "))
#   i += 1
# print(ingredients)

# def get_ingredients():
#     recipe = input("What are we making?: ")
#     count = int(input("How many ingredients?: "))
#     ings = []
#     qtts=[]
#     i = 1
#     while i <= count:
#         ing = input('Enter ingredient '+ str(i) + ': ')
#         ings.append(ing)
#         q = input('Enter ingredient ' + str(i) +  ' quantity : ')
#         qtts.append(q)
#         i+= 1
#     return ings, qtts
#
# print(get_ingredients())

recipe = input("What are we making?: ")
count = int(input("How many ingredients?: "))
ings = []
qtts = []
i = 1
while i <= count:
    ing = input('Enter ingredient ' + str(i) + ': ')
    ings.append(ing)
    q = input('Enter ingredient ' + str(i) + ' quantity : ')
    qtts.append(q)
    i += 1

print(ings, qtts)
