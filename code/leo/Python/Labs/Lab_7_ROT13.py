
ROT13 = {
    'a' : 'n',
    'b' : 'o',
    'c' : 'p',
    'd' : 'q',
    'e' : 'r',
    'f' : 's',
    'g' : 't',
    'h' : 'u',
    'i' : 'v',
    'j' : 'w',
    'k' : 'x',
    'l' : 'y',
    'm' : 'z',
    'n' : 'a',
    'o' : 'b',
    'p' : 'c',
    'q' : 'd',
    'r' : 'e',
    's' : 'f',
    't' : 'g',
    'u' : 'h',
    'v' : 'i',
    'w' : 'j',
    'x' : 'k',
    'y' : 'l',
    'z' : 'm',
    ' ' : ' '
}
code = []

user_string = input("Enter a sequence of letters to encode or decode: ")
user_string = user_string.lower() #input string into lower case

try: # using try and except in case user chooses number or character not in the dicionary.
    user_string_list = [x for x in user_string] #input into a list of keys
    for x in user_string:
        code.append(ROT13[x]) #with a list of keys, create a list of values

    print(f"The encode input is :  {''.join(code)}") #list  into string
 
except KeyError: #in case of characters not in the dictionary print msn 
    print(f'You entered "{user_string}", this program only encode "letters".') 



