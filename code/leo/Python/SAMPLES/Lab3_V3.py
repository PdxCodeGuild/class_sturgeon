#Verion 3

measurements = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

measurements['yard'] = 0.9144
measurements['inch'] = 0.0254

distance = float(input('what is the distance? '))

unit = (input('what are the units ft, mi, m, km, yard, or inch? '))

answer = distance * measurements[unit]

print(f'{distance} {unit} is {answer} m')