#Version 1 

feet_multiplier = 0.3048

feet_input = float(input("What is the distance in feet? "))
meter_output = round((feet_input * feet_multiplier), 3)

print(f"{feet_input} ft is {meter_output} m.")

#Version 2
#Dictionary aiding in meter conversion
meter_multiplier = {
    "feet" : 0.3048,
    "miles" : 1609.34,
    "meters" : 1,
    "kilometers" : 1000
}
#Asks the user to input the distance and units
distance_input = float(input("What is the distance? "))
unit_input = input("What are the units? Please input feet, miles, meters, kilometers, yards, inches: ")

#Makes sure that unit type inputed can be converted
unit_checker = ["feet", "miles", "meters", "kilometers"]

#Version3 added here to aid support, string in unit_input also amended
#Adds new key:value pairs to meter_multiplier
meter_multiplier.update({"yards" : .9144, "inches" : 0.0254})

unit_checker.append("yards")
unit_checker.append("inches")

#cont. of Version 3
#Uses the unit checker as a key idenfier to make the conversion
if unit_input in unit_checker:
    convertor = meter_multiplier[unit_input]
    conversion_output = distance_input * convertor
else:
    print("Please select an appropriate unit of measurement.")
#prints result to terminal
print(f"{distance_input} {unit_input} is/are {round(conversion_output, 3)} meters")

#Version4
#Asks users for their inputs
user_distance = float(input("What is the distance? "))
user_unit = input("What are the units? Please input feet, miles, meters, kilometers, yards or inches: ")
out_unit = input("What are the output units? Please input feet, miles, meters, kilometers, yards or inches: ")

#converts to meters
if user_unit in unit_checker:
    meter_convertor = meter_multiplier[user_unit]
    meter_output = user_distance * meter_convertor
else:
    print("Please select an appropriate unit of measurement.")

#Convert meters to selected units
if out_unit in unit_checker:
    final_convertor = meter_multiplier[out_unit]
    final_output = round((meter_output / final_convertor), 4)
else:
    print("Please select an appropriate unit of measurement.")

#prints final statement
print(f"{user_distance} {user_unit} is {final_output} {out_unit}.")
