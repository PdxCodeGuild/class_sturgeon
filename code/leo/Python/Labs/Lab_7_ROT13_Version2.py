

characters = [
    'a',
    'b',
    'c',
    'd', 
    'e', 
    'f', 
    'g', 
    'h', 
    'i', 
    'j', 
    'k', 
    'l', 
    'm', 
    'n', 
    'o', 
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
    ]

code = []

user_string = input("Enter a sequence of letters to encode: ")
user_string = user_string.lower() #input string into lower case
user_string = user_string.replace(' ', '') #clean up empty spaces

user_rotation = int(input('Enter the number of rotation to encode: ')) #ask user for rotations

user_string_list = [x for x in user_string] #input string letters into single items in a list

try: # avoid items that are not on the list
    for x in user_string:
        user_string_index = int(characters.index(x)) #items list into index numbers
        location = user_string_index + user_rotation #add input item index location plus user choice of rotation 
        
        if location <= 25:  # in case location index is on the list
            code.append(characters[location]) 
        
        else: 
            location = location - 26 # in case index is larger than list ( if needed, add more elif for very large numbers)
            code.append(characters[location]) 

    print(f"The encode input is :  {''.join(code)}") #list into string

except (IndexError, ValueError): #in case of items not on the list 
    print(f'You entered "{user_string}", this program only encode "letters".') 
    
