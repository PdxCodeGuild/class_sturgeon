#Lab 6: Credit Card Validation
#Write a function which returns whether a string containing a cc# is valid as a boolean
import time

print("")
welcome_message = "Welcome to the Library-Interface's Credit-Card Validator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
time.sleep(.5)
print("")

def credit_validation(card_number:str):
    card_map = map(int, card_number) #make str input ints using map(argument1, argument2)
    card_list = list(card_map) #Step 1: convert to list
    print(card_list) #shows all 16 numbers on cc
    check_digit = card_list[15] #Create a variable for Step 8: Check digit against end number for validation
    x = slice(0, 15) #16 digits becomes 15 by ending the slice one before the end
    card_list = card_list[x] #Step 2: Slicing the 16th digit off
    print(card_list)
    card_list.reverse() #Step 3: Reverse the digits
    print(card_list) 
    card_list[0::2] = [x*2 for x in card_list[0::2]] #Step 4: Double every other element
    print(card_list)
    card_list = [card - 9 if card > 9 else card for card in card_list] #Step 5: minus 9 on all numbers over 9
    print(card_list)
    total = sum(card_list) #Step 6: Sum up all the values
    print(total)
    second_digit = total % 10 #Step 7: Get the second number
    print(second_digit)
    time.sleep(1)
    if check_digit == second_digit: #Step 8: Card is valid or it's not
        print("Valid")
    else:
        print("Invalid")
    return second_digit == check_digit #Get a boolean response

while True:
    try:
        card_number = input("Enter 16-digit Credit Card Number with no spaces:-->").strip()
        time.sleep(.5)
        if len(card_number) == 16:
            credit_validation(card_number)
            time.sleep(1.5)
            if input("Enter another Credit Card Number? (Yes/No)-->").lower() != "yes":
                break
            time.sleep(.5)
        else:
            print("Error, not a 16 digit number!")
    except:
        print("You need to enter a 16 digit credit card-->")
time.sleep(.5)
print("")
print("Thank you for using the Library-Interface's Credit-Card Validator.")

#Alternate method from Merritt Lawrenson
    # def cc_valid(original_number):
    #     list_of_ints = [int(num) for num in original_number]
    #     check_digit = list_of_ints.pop()
    #     reversed_digits = list(reversed(list_of_ints))
    #     every_other_doubled = [digit * 2 if i % 2 == 0 else digit for i, digit in enumerate(reversed_digits)]
    #     subtract_nine = [digit - 9 if digit > 9 else digit for digit in every_other_doubled]
    #     digit_sum = sum(subtract_nine)
    #     second_digit = digit_sum % 10
    #     return second_digit == check_digit