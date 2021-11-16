year2021 = {
    'jan': 31,
    'feb': 28,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31,
}

month = 0
x = True

while x == True :
    month = input('Enter the name of a month to see how many days are in it or "done" to quit month: ')

    if month != 'done':
        days = year2021[month.lower()]
        print(f'{month} has {days} days in it.')
    
    elif month == 'done':
        x = False
     
print('Thanks, bye')