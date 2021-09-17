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
    # Need to do this by index, not number value
    doubled_odds = [n * 2 if n % 2 == 1 else n for n in num_list]
    print(doubled_odds)

    # if a number is over 9, subtracting 9 from it
    under_nine = [n - 9 if n > 9 else n for n in doubled_odds]
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





credit_card = '4556737586899855'

print(credit_card_validator(credit_card))



