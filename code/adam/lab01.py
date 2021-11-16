#Unit Converter
import time

#Version 1
#ask user to enter number of feet and print out equivalent distance in meters. 1 ft = 0.3048m

# feet = float(input("Enter number of feet to convert to meters-->"))
# meter = feet * 0.3048
# time.sleep(.5)
# print("There are " + str(feet) + " feet in " + str(meter) + " meters")

#Version 2
#User also enters feet, miles meter and kilometers to convert to meters

# unit = input("Enter the unit of measurement to convert to meters (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles-->")
# number = float(input("Enter number to convert to meters-->"))
# if unit == "f":
#     total = number * 0.3048
# if unit == "k":
#     total = number * 1000
# if unit == "mi":
#     total = number * 1609.34
# if unit == "m":
#     total = number
# total = str(total)
    
# time.sleep(.5)
# print("There result is " + total + " meters")

#Version 3
#add support for yard and inches

# unit = input("Enter the unit of measurement to convert to meters (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, (in) for inches-->")
# number = float(input("Enter number to convert to meters-->"))
# if unit == "f":
#     total = number * 0.3048
# if unit == "k":
#     total = number * 1000
# if unit == "mi":
#     total = number * 1609.34
# if unit == "m":
#     total = number
# if unit == "y":
#     total = number * 0.9144
# if unit == "in":
#     total = number * 0.0254
# total = str(total)
    
# time.sleep(.5)
# print("There result is " + total + " meters")

#Version 4
#Ask user for distance, starting units, and units to convert to. We'll convert everything to meters and go from there.

# unit = input("Enter the unit of measurement to convert from (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, (in) for inches-->")
# number = float(input("Enter number to convert-->"))
# unit2 = input("What would you like to convert the distance to? (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, (in) for inches-->")
# if unit == "f":
#     total = number * 0.3048
# if unit == "k":
#     total = number * 1000
# if unit == "mi":
#     total = number * 1609.34
# if unit == "m":
#     total = number
# if unit == "y":
#     total = number * 0.9144
# if unit == "in":
#     total = number * 0.0254

# if unit2 == "f":
#     final = total * 1/0.3048
# if unit2 == "k":
#     final = total * 1/1000
# if unit2 == "mi":
#     final = total * 1/1609.34
# if unit2 == "y":
#     final = total * 1/0.9144
# if unit2 == "in":
#     final = total * 1/0.0254

# final = str(final)
# time.sleep(.5)
# print("There result is " + final)

#Version 5
#Make it pretty and idiot-proof

message = "Welcome to the Library-Interface's Unit Converter"
for char in message:
  print(char, end='', flush=True)
  time.sleep(.1)
print("")
unit = input("Enter the unit of measurement to convert from: (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, (in) for inches-->").lower()
while not (unit == 'm' or unit == 'meters' or unit == 'k' or unit == 'f' or unit == 'feet' or unit == 'mi' or unit == 'miles' or unit == 'y' or unit == 'yards' or unit == 'in' or unit == 'inches'):
    unit = input('That is an invalid choice. Enter (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, or (in) for inches-->')
time.sleep(.2)
# number = float(input("Enter number to convert-->"))

while True:
    number = input('Enter number to convert-->')
    try:
        number = float(number)
        if number > 0:
            break
        else:
            print('The number must be greater than zero')
    except:
        print('Invalid number, try again')

time.sleep(.2)
unit2 = input("What would you like to convert the distance to? (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, (in) for inches-->")
while not (unit2 == 'm' or unit2 == 'k' or unit2 == 'f' or unit2 == 'mi' or unit2 == 'y' or unit2 == 'in'):
    unit2 = input('That is an invalid choice. Enter (m) for meter, (k) for kilometer, (f) for feet, (mi) for miles, (y) for yard, or (in) for inches-->')

if unit == "f":
    unit = "Feet"
    total = number * 0.3048
if unit == "k":
    unit = "Kilometers"
    total = number * 1000
if unit == "mi":
    unit = "Miles"
    total = number * 1609.34
if unit == "m":
    unit = "Meters"
    total = number
if unit == "y":
    unit = "Yards"
    total = number * 0.9144
if unit == "in":
    unit = "Inches"
    total = number * 0.0254
#now convert from meters to other selected unit
if unit2 == "f":
    unit2 = "Feet"
    final = total * 1/0.3048
if unit2 == "k":
    unit2 = "Kilometers"
    final = total * 1/1000
if unit2 == "mi":
    unit2 = "Miles"
    final = total * 1/1609.34
if unit2 == "y":
    unit2 = "Yards"
    final = total * 1/0.9144
if unit2 == "in":
    unit2 = "Inches"
    final = total * 1/0.0254

final = str(final)
number = str(number)
time.sleep(.5)
print("The " + number + " of " + unit + " that you entered equals " + final + " " + unit2)
message2 = "Thank you for using Library-Interface's Converter"
for char in message2:
  print(char, end='', flush=True)
  time.sleep(.1)