# rot cipher

import string


def rot_cipher (rotation, str):
    abc_list = list(string.ascii_lowercase)
    
    
    str = list(str)
    print(str)
    new_word = ''
    for i in str:
        new_index = abc_list.index(i) + rotation
        if new_index >= 26:
            new_index -= 26
        new_word += abc_list[new_index]
    return new_word
    
rot = int(input('How much rotation would you like to use? '))
user_str = input('What word would you like to encrypt? ')
print(rot_cipher(rot, user_str))
