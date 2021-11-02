def card_validator():
    card_num = list(input('Enter a card number: '))
    
    check_digit = int(card_num.pop())
    
    reversed_card = card_num[::-1]
    
    double = [int(num)*2 if i%2==0 else int(num) for i, num in enumerate(reversed_card)]
    
    nines = [num-9 if num>9 else num for num in double]

    total = sum(nines)

    second_digit = total%10

    if second_digit == check_digit:
        return True
        
    else:
        return False

#return second_digit == check_digit for boolean
if card_validator() == True:
    print('Valid!')
else: print('Invalid entry..')


