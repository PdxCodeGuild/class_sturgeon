"""Lab 6"""
#cc_number = "4556737586899855" for Testing purposes

cc_number = input(f"Please input a credit card number and I will check if its valid: ")

def valid_credit_card(card_number):
    step_1 = [int(digits) for digits in cc_number]

    check_digit = step_1[-1]
    sliced_list = step_1[:-1]
    reversed_list = sliced_list[::-1]

    doubled = []
    for index, value in enumerate(reversed_list):
        if index%2 == 0: 
            value *= 2
            doubled.append(value)
        else:
            doubled.append(value)                

    niner = []    
    for x in doubled:
        if x > 9:
            niner.append(x-9)
        elif x <= 9:
            niner.append(x)

    list_sum = 0 
    for each in niner:
        list_sum += each

    second_digit = list_sum%10

    if second_digit == check_digit:
        print("Valid!")
    else:
        print("Not valid!")

valid_credit_card(cc_number)