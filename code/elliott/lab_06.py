
def validator():
    credit_card = [int(digits)
                   for digits in input("Enter your credit card number: ")]
    digits = credit_card
    check_digit = credit_card.pop(15)
    digits.reverse()
    digits[::2] = [x*2 for x in digits[::2]]
    digits = [x-9 if x >= 10 else x for x in digits]
    sum_digits = sum(digits)
    x = [int(a) for a in str(sum_digits)]
    val_digit = x.pop()
    if val_digit == check_digit:
        print("your card is valid!")


validator()
