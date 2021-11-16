# number to phrase

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
    #print(num, 'num')
    
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
user_num = input('What number would you like to convert to English? 0-999: ')
user_num = int(user_num)

# seperating ones, teens, tens, and hundreds
hundreds_digit = user_num//100
tens_digit = (user_num//10)%10
teens_digit = user_num - (hundreds_digit * 100)
ones_digit = user_num%10

# converting number input to english
ones_phrase = convert_ones(ones_digit)
teens_phrase = convert_teens(teens_digit)
tens_phrase = convert_tens(tens_digit)
hundreds_phrase = convert_hundreds(hundreds_digit)

# logic on how to print correct phrases
# can this be a function?
#print(teens_phrase)

if user_num < 10:
    print(f'The number {user_num} is "{ones_phrase}" in English')

elif user_num < 100:
    if tens_digit == 1:
        print(f'The number {user_num} is "{teens_phrase}" in English')
    elif ones_digit == 0:
        print(f'The number {user_num} is "{tens_phrase}" in English')
    else:
        print(f'The number {user_num} is "{tens_phrase}-{ones_phrase}" in English')

# issues with the hundreds-phrase returning None in the tens place
# also... how to deal with the teens in the hundreds section?

elif user_num < 1000:
    if ones_digit == 0 and tens_digit == 0:
        print(f'The number {user_num} is "{hundreds_phrase}" in English')
    elif tens_digit == 0:
        print(f'The number {user_num} is "{hundreds_phrase} and {ones_phrase}" in English')
    elif tens_digit == 1:
        print(f'The number {user_num} is "{hundreds_phrase} and {teens_phrase}" in English')
    elif tens_digit > 1 and ones_digit == 0:
        print(f'The number {user_num} is "{hundreds_phrase} and {tens_phrase}" in English')
    else:
        print(f'The number {user_num} is "{hundreds_phrase} and {tens_phrase}-{ones_phrase}" in English')

