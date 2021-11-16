# #How to capitalize a list:

# #make a list
# fruits = "apples, bananas, pears, pinapples, pizza"
# fruit_list = fruits.split(', ')
# fruit_list.insert(1, "oranges")
# fruit_list.pop(-1)
# #now to capitalize the list
# fruit_capitalize = ' - '.join(fruit_list).upper()
# fruit_list_upper = fruit_capitalize.split(', ')
# fruit_list_lower = fruit_list.copy()
# fruit_list_lower = ' - '.join(fruit_list_lower)
# fruit_list_lower = fruit_list_lower.split(', ')
# fruit_list_lower.sort()
# fruit_list_upper.sort()
# print(fruit_list_upper)
# print(fruit_list_lower)

# for i in range(len(fruit_list_upper)):
#     print(fruit_list_upper[i])

# for j in range(len(fruit_list_lower)):
#     print(fruit_list_lower[j])

# print(list(enumerate(fruit_list)))

# for i, fruit in enumerate(fruit_list):
#     print(i, fruit)

# def say_hello():
#     print('hello!')
# say_hello()
# import math

# romanMatrix = [
#   [1000, 'M'],
#   [900, 'CM'],
#   [500, 'D'],
#   [400, 'CD'],
#   [100, 'C'],
#   [90, 'XC'],
#   [50, 'L'],
#   [40, 'XL'],
#   [10, 'X'],
#   [9, 'IX'],
#   [5, 'V'],
#   [4, 'IV'],
#   [1, 'I']
# ]

# def convertToRoman(num): 
#     if (num == 0):
#         return ""
#     for (i == 0, i < len(romanMatrix), i++):
#     if (num >= romanMatrix[i][0]) 
#       return romanMatrix[i][1] + convertToRoman(num - romanMatrix[i][0])
    

#found this on the web, don't know how it works. Study time...  
# class py_solution:
# def int_to_Roman(num):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#         ]
#     syb = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#         ]
#     roman_num = ''
#     i = 0
#     while num > 0:
#         for _ in range(num // val[i]):
#             roman_num += syb[i]
#             num -= val[i]
#         i += 1
#     return roman_num
# print(int_to_Roman(3))


fruits = {'apple': 1.0, 'pear': 1.5}

fruit = input("Enter a new fruit to add: ")
price = input(f"enter the price for {fruit}: ")
fruits[fruit] = price

print("")

for x in fruits.keys():
    print(x)

print("")

for x in fruits:
    print(x)

print("")

for x in fruits.items():
    print(x)

print("")

for key, value in fruits.items():
    print(key)
    print(value)

print("")