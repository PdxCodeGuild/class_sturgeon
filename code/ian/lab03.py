
numbers = {
    'ones' : {
        1:'one',
        2:'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine'
    },
    'teens' : {
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen'
        
    },
    'tens' : {
        2:'twenty',
        3:'thirty',
        4:'fourty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety'
    }
    }


x = int(input('Enter a number: '))
hundreds_digit = x//100
tens_digit = x//10
ones_digit = x%10

if x == 0:
    print('zero')

elif x < 10:
    print(f'{numbers["ones"][x]}')

elif x in numbers['teens']:
    print(numbers['teens'][x])

elif 19 < x < 100:
    if ones_digit == 0:
        print(numbers["tens"][tens_digit])
    else:    
        print(f'{numbers["tens"][tens_digit]}-{numbers["ones"][ones_digit]}')

elif x > 99:
    new_tens = tens_digit%10
    new_teens = x%100

    if new_teens in numbers['teens']:
        print(f'{numbers["ones"][hundreds_digit]} hundred {numbers["teens"][new_teens]}')
    elif ones_digit == 0:
        if new_tens == 0:
            print(f'{numbers["ones"][hundreds_digit]} hundred')
        else:
            print(f'{numbers["ones"][hundreds_digit]} hundred {numbers["tens"][new_tens]}')
    elif new_tens == 0:
        print(f'{numbers["ones"][hundreds_digit]} hundred and {numbers["ones"][ones_digit]}')
    
    else:
        print(f'{numbers["ones"][hundreds_digit]} hundred {numbers["tens"][new_tens]}-{numbers["ones"][ones_digit]}')



