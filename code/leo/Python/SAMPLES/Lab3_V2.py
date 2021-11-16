#Verion 2

measurements = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

distance = float(input('what is the distance? '))

unit = (input('what are the units ft, mi, m, or km? '))

answer = distance * measurements[unit]

print(f'{distance} {unit} is {answer} m')
