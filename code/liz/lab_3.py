

# converting ones to an english phrase
def convert_ones (num):
    if num == 0:
        return 'zero'
    if num == 1:
        return 'one'
    if num == 2:
        return 'two'
    if num == 3:
        return 'three'
    if num == 4:
        return 'four'
    if num == 5:
        return 'five'
    if num == 6:
        return 'six'
    if num == 7:
        return 'seven'
    if num == 8:
        return 'eight'
    if num == 9:
        return 'nine'

# converting teens to an english phrase
def convert_teens (num):
    if num == 10:
        return 'ten'
    if num == 11:
        return 'eleven'
    if num == 12:
        return 'twelve'
    if num == 13:
        return 'thirteen'
    if num == 14:
        return 'fourteen'
    if num == 15:
        return 'fifteen'
    if num == 16:
        return 'sixteen'
    if num == 17:
        return 'seventeen'
    if num == 18:
        return 'eighteen'
    if num == 19:
        return 'nineteen'

# converting tens to an english phrase
def convert_tens (num):
    if num == 2:
        return 'twenty'
    if num == 3:
        return 'thirty'
    if num == 4:
        return 'forty'
    if num == 5:
        return 'fifty'
    if num == 6:
        return 'sixty'
    if num == 7:
        return 'seventy'
    if num == 8:
        return 'eighty'
    if num == 9:
        return 'ninety'

# converting hundreds to an english phrase
def convert_hundreds (num):
    if num == 1:
        return 'one hundred'
    if num == 2:
        return 'two hundred'
    if num == 3:
        return 'three hundred'
    if num == 4:
        return 'four hundred'
    if num == 5:
        return 'five hundred'
    if num == 6:
        return 'six hundred'
    if num == 7:
        return 'seven hundred'
    if num == 8:
        return 'eight hundred'
    if num == 9:
        return 'nine hundred'

# number input... maybe make user input?
x = 111

# seperating ones, tens, and hundreds
hundreds_digit = x//100
tens_digit = x//10
ones_digit = x%10

# converting number input to english
ones_phrase = convert_ones(ones_digit)
teens_phrase = convert_teens(x)
tens_phrase = convert_tens(tens_digit)
hundreds_phrase = convert_hundreds(hundreds_digit)

# logic on how to print correct phrases
# can this be a function?
if len(str(x)) == 1:
    print(ones_phrase)
elif len(str(x)) == 2:
    if tens_digit == 1:
        print(teens_phrase)
    else:
        print(f'{tens_phrase}-{ones_phrase}')

# issues with the hundreds-phrase returning None in the tens place
# also... how to deal with the teens in the hundreds section?
elif len(str(x)) == 3:
    print(f'{hundreds_phrase} and {tens_phrase}-{ones_phrase}')