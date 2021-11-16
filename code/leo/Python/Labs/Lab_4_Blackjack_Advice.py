values = {
    'A': 1,
    'a': 1,
    'J': 10,
    'j': 10,
    'Q': 10,
    'q': 10,
    'K': 10,
    'k': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
}

card1 = input("What's your firt card? ")
card1 = int(values[card1])

card2 = input("What's your second card? ")
card2 = int(values[card2])

card3 = input("What's your third card? ")
card3 = int(values[card3])

answer = card1 + card2 + card3

if answer < 17:
    print(f'{answer} "Hit"')

elif answer >= 17 and answer < 21:
    print(f'{answer} "Stay"')

elif answer == 21:
    print(f'{answer} "Blackjack!"')

elif answer < 21:
    print(f'{answer} "Already Busted"')
