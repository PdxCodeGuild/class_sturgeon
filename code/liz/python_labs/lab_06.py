# credit card validation

def credit_card_validator (card_num):
    # converting input string into list of ints
    num_list = [int(num) for num in card_num]
    print(num_list)

    # slicing off the last digit
    check_digit = num_list.pop()
    print(check_digit)

    # reversing the digits in the list
    num_list.reverse()
    print(num_list)

    # doubling every other element in the reversed list
    doubled_evens = [n * 2 if i % 2 == 0 else n for i, n in enumerate(num_list)]
    print('doubled evens', doubled_evens)

    # if a number is over 9, subtracting 9 from it
    under_nine = [n - 9 if n > 9 else n for n in doubled_evens]
    print(under_nine)

    # summing up all the numbers in the list. Is there a way to do list comprehension for this?
    lst_sum = 0
    for num in under_nine:
        lst_sum += num
    second_digit = lst_sum % 10
    print(lst_sum)

    # checking if the second digit of the sum == the check digit
    if second_digit == check_digit:
        return 'This credit card is valid!'
    else:
        return 'This credit card is not valid'





credit_card = input('Please enter the credit card number you want to check: ')

print(credit_card_validator(credit_card))



