card_values1 = {
    'a' : 1,
    'A' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'j' : 10,
    'J' : 10,
    'q' : 10,
    'Q' : 10,
    'k' : 10,
    'K' : 10
}
card_values2 = {
    'a' : 11,
    'A' : 11,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10,
    'j' : 10,
    'J' : 10,
    'q' : 10,
    'Q' : 10,
    'k' : 10,
    'K' : 10
}

card_1_key = input('What\'s your first card? ')
card_2_key = input('What\'s your second card? ')
card_3_key = input('What\'s your third card? ')
card_1 = card_values2[card_1_key]
card_2 = card_values2[card_2_key]
card_3 = card_values2[card_3_key]

total = card_1 + card_2 + card_3

if total < 17:
    print(f'{total} Hit')
elif total >= 17 > 21:
    print(f'{total} Stay')
elif total == 21:
    print(f'{total} Blackjack!')
elif total > 21:
    card_1 = card_values1[card_1_key]
    card_2 = card_values1[card_2_key]
    card_3 = card_values1[card_3_key]
    total = card_1 + card_2 + card_3
    
    if total < 17:
        print(f'{total} Hit')
    elif total >= 17 > 21:
        print(f'{total} Stay')
    elif total == 21:
        print(f'{total} Blackjack!')
    elif total > 21:
        print(f'{total} Already Busted..')

