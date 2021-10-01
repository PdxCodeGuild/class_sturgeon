
num = float(input('Enter a number: '))
unit = input('Enter the unit ft, mi, m, yard, inch or ki:')
out = input('What are the output units?')

ft = 0.3048
mi = 1609.34
m = 1
km = 1000
yard = 0.9144
inch = 0.0254


conv = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
}


first_conv = num * conv.get(unit)
final = first_conv / conv.get(out)

print(f'{num} {unit} is {final} {out}')
