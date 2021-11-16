'''
1.2
Create variables with numbers representing the base and height measurements of the triangle. Select a, b or c to represent the base.

Calculate the area of the triangle.
'''
#area
a = float(input('Enter the base measurement of the triangle: '))
b = float(input('Enter the height measurement of the triangle: '))

x = a * b / 2

print(f'A triangle with a base of {a} and a heoght of {b} has an area of {x} .')
