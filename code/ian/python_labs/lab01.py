# Unit Converter

#establish conversion to meter dictionary
conversions = {
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000,
    'yard' : 0.9144,
    'in' : 0.0254
}

#ask user for input distance
distance_in = int(input('What are the units?\n'))

#ask user for unit input
units_in = input('What are the units?\n')  

#ask user for unit output
units_out = input('What units would you like to convert to?\n')

#convert distance in to meters
distance_out = distance_in * conversions[units_in]

#convert meter distance to unit out distance
new_distance_out = distance_out / conversions[units_out]

#print result with f string and round to second decimal
print(f'{distance_in} {units_in} is {new_distance_out:.2f} {units_out}')