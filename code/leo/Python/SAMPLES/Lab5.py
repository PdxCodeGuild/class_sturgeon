import random
import string

character = string.ascii_letters + string.digits + string.punctuation

password = []

for list_character in range(11) :
    password.append(random.choice(character))

print(password)


#print(''.join(password))



#while len(character) < 11

#computer = random.choice(character)

#print(character)