import random
import string

character = string.ascii_letters + string.digits + string.punctuation

password = []

while len(password) <10 :
    password.append(random.choice(character))

print("Your password is: ", ''.join(password))