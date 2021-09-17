def card_validator():
    #1
    card_num = list(input('Enter a card number: '))
    
    #2
    check_digit = int(card_num.pop())
    
    #3
    reversed_card = card_num[::-1]
    
    #4
    double = [int(num)*2 if i%2==0 else int(num) for i, num in enumerate(reversed_card)]
    
    #5
    nines = [num-9 if num>9 else num for num in double]

    #6
    total = sum(nines)

    #7
    second_digit = total%10

    #8
    if second_digit == check_digit:
        print('Valid!')
        
    else:
        print('Invalid card number..')

card_validator()