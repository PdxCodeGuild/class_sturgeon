#Lab 7: ROT Cipher
#Version 1: Rotate the characters 13 times
#Version 2: Allow user to specify rotation amount
#Decrytper: Works with version 1 only as it just adds 13 more, bringing full circle the ROT13.
import time

print("")
welcome_message = "Welcome to the Library-Interface's ROT Encryption"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
print("")

alphabet = "abcdefghijklmnopqrstuvwxyz"

def lab07v1(userinput):
    encrypted_output = ""

    for char in userinput:
        encrypted_output += alphabet[(alphabet.find(char)+13)%26]
    return encrypted_output

# print("")
# print(lab07v1(input("Enter a word to be encrypted using version 1:-->")))

def lab07v2(userwords, shift_number):
    variable_encryption = ""
    # shift_number = int(input("Enter a number for the encryption rotation:-->"))

    for char in userwords:
        variable_encryption += alphabet[(alphabet.find(char)+shift_number)%26]
    print(f"Encrypting '{userwords}'")
    encrypting = "........\n........\n........"
    for char in encrypting:
        print(char, end='', flush = True)
        time.sleep(.1)
    print("")
    print(f"Your encrypted word is: '{variable_encryption}'")
    return variable_encryption

while True:
    try:
        userwords = input("Enter a word to be encrypted using version 2:-->")
        if userwords.isalpha():
            user_number = input("Enter a number for the encryption rotation:-->")
            if user_number.isdigit():
                user_number = int(user_number)
                if user_number > 0 and user_number < 26:
                    lab07v2(userwords, user_number)
                    if input("Use Version 2 Again? (Yes, No)-->").lower() != "yes":
                        break
                else: print("The number needs to be between 1 and 25, start over.")
                continue
            else: print("You must enter a number without letters, start over.")
        else: print("You need to enter a word without numbers.")
    except:
        print("Contact Help Desk")

def decrypt(secret):
    secret_word = ""

    for char in secret:
        secret_word += alphabet[(alphabet.find(char)+13)%26]
    return secret_word

# print("")
# print(decrypt(input("Enter a word to decrypt:-->")))

print("")
goodbye_message = "Thank you for using Library-Interface's ROT Encryption"
for char in goodbye_message:
  print(char, end='', flush=True)
  time.sleep(.02)