ONEtoNINE = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

TENtoNINETEEN = {
    1.0: 'ten',
    1.1: 'eleven',
    1.2: 'twelve',
    1.3: 'thirteen',
    1.4: 'fourteen',
    1.5: 'fifteen',
    1.6: 'sixteen',
    1.7: 'seventeen',
    1.8: 'eighteen',
    1.9: 'nineteen',
}

TWENTYtoNINETY = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}
a = ""
b = ""
c = ""

user_choice_of_number = int(input('Enter a number between 0 and 999: '))

if user_choice_of_number <= 0:
    print("zero")
    
else:
 
    lOOs = user_choice_of_number // 100
    lOs = (user_choice_of_number % 100) // 10
    TEENS = (user_choice_of_number % 100) / 10
    ls = user_choice_of_number % 10

    if lOOs > 0:
        a = ONEtoNINE[lOOs] + " " + "hundred"

    if lOs > 1.9:
        b = " " + TWENTYtoNINETY[lOs]
     
    if TEENS > 0.9 and TEENS < 2:
        b = " " + TENtoNINETEEN[TEENS]

    elif ls > 0:
        c = " " + ONEtoNINE[ls]
    

    print(f"{a}{b}{c}")
    
