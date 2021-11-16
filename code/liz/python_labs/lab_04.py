# blackjack advice


# function to convert face cards to numeric values
def face_card_converter (cards):
    new_cards = []
    for card in cards:
        if card == 'J':
            new_cards.append(10)
        elif card == 'Q':
            new_cards.append(10)
        elif card == 'K':
            new_cards.append(10)
        elif card == 'A':
            new_cards.append(1)
        else:
            new_cards.append(int(card))
    return new_cards



# function to give blackjack advice
def blackjack_advice (cards):
    cards_sum = 0
    for card in cards:
        cards_sum += card
    if cards_sum < 17:
        return f'{cards_sum} Hit'
    elif cards_sum >= 17 and cards_sum < 21:
        return f'{cards_sum} Stay'
    elif cards_sum == 21:
        return f'{cards_sum} Blackjack!'
    else:
        return f'{cards_sum} Already Busted'



#Tell user options and get three input values
print('Your card options are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K')

first_card = input('What is your first card? ')
second_card = input('What is your second card? ')
third_card = input('What is your third card? ')

# add cards to empty list
cards = []
cards.append(first_card)
cards.append(second_card)
cards.append(third_card)

# enter user values into converter function then put that value in advice function and print
card_values = face_card_converter(cards)
advice = blackjack_advice(card_values)

print(advice)

