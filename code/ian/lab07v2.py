# establish list with starting index
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ask for input letter and convert to list
letters_in = list(input('Enter a message: '))
rot = int(input('Level of security: '))


letters_index_list = []

for l in letters_in:
    
    letters_index = letters_index_list.append(english.index(l))
    


message = []
for num in letters_index_list:
    try:
        new_letter = english[num + rot]
        message.append(new_letter)
    except IndexError:
        new_letter = english[num - rot]
        message.append(new_letter)

message = ''.join(message)
print(message)

