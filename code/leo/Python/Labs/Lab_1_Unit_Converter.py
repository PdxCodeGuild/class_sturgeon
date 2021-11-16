

measurements = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}

distance = float(input('what is the distance? '))

input_unit = (input('what are the input unit ft, mi, m, km, yard, or inch? '))

meter_convertion = distance * measurements[input_unit] # cover input distance to meter

output_unit = (input('what are the output units unit you are looking for ft, mi, m, km, yard, or inch? '))

if output_unit == "ft":
    answer = float(meter_convertion * 3.28084)

elif output_unit == "mi":
    answer = float(meter_convertion * 0.000621371)

elif output_unit == "m":
    answer = meter_convertion

elif output_unit == "km":
    answer = float(meter_convertion * 0.001)

elif output_unit == "yard":
    answer = float(meter_convertion * 1.09361)

elif output_unit == "inch":
    answer = float(meter_convertion * 39.3701)

print(f'{distance} {input_unit} is {answer} {output_unit}')