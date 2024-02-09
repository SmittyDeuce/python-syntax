import math
# # 1)
# # task 1
# weather = "sunny"

# if weather == "sunny":
#     print("Wear sunglasses!")
# else:
#     print("Take an umbrella!")

# # task 2
    
# feeling = input("how are you feeling? ")
# if feeling == 'happy':
#     print("That's great to hear!")
# elif feeling == 'sad':
#     print("I hope your day gets better!")
# # task 3
    
# mood = "excited"

# if mood == "excited":
#     print("Yay! Let's have fun.")
# else:
#     print("Let's find something fun to do!")

# # 2)
# # task 1
    
# # Python, oh Python, so clear and so neat
# # With every new challenge, you're hard to beat.
# # easy for newcomers in the world of code
# # dyanmic typing makes reassignment a breeze
# # top 3 most used language in the programming world

# # task 2
    
# '''
# Python, in the realm of code you shine,
# With simplicity and grace, you're truly divine.
# no need for anchors as you're not html
# makes typing so quick when you don't need brackets
# Python you're in a whole different bracket
# ...
# '''

# # task 3

# # this line is from my first poem
# # dyanmic typing makes reassignment a breeze

# # this line is from my multi-line poem
# '''
# Python you're in a whole different bracket
# '''
# # 3)

# PI_VALUE = 3.14
# UserAge = 25
# user_location = "New York"
# MAX_LIMIT = 1000

# # 4)

# variable_a = "Hello, World!" # str
# variable_b = 23 # int
# variable_c = 3.14 #float
# variable_d = True #boolean

# print(type(variable_a))
# print(type(variable_b))
# print(type(variable_c))
# print(type(variable_d))

# # 5)

# dynamic_variable = "This is a string"
# print(type(dynamic_variable))

# dynamic_variable = 100
# print(type(dynamic_variable))

# dynamic_variable = 25.5
# print(type(dynamic_variable))

# # 6) 
# # task 1.
# item1 = 2.00
# item2 = 4.00
# item3 = 1.97
# print( item1 + item2 + item3)

# # task 2
# principal = 300
# rate = 3
# time = 1
# amount = principal * (1 + rate/100) ** time
# print(amount)

# # task 3
# length = 13
# width = 18
# rectangle_area = length * width 
# rectangle_perimeter = length*2 + width*2
# print('A:',rectangle_area, 'P:',rectangle_perimeter)

# 7)
# task 1
# num1 = 10
# num2 = 2
# print(num1 > num2)
# # print(num1, num2)
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1 > num2)
# # print(num1, num2)

# task 2
# def is_it_perfect_square(number):
#     if number <= 0:
#         return False
#     square_root = number ** .5
    
#     print(square_root)
#     print(int(square_root))
#     if square_root == int(square_root):
#         return True
#     else: 
#         return False
    
# print(is_it_perfect_square(64))
# print(is_it_perfect_square(65))

# 8)
# task 1
element1 = True
element2 = True
element3 = False
element4 = False

print(element1 and element4)
print(element1 or element4)
print(element1 and not element4)
print(element1 and element3)
print(element1 and element3 or element4 and element2)

# task 2
print( 9 * 4 + 5)
print(9 * (4 + 5))

# task 3
res = 28 / 4 > 2 and 28 / (4 / 2) == 2
print(res)
