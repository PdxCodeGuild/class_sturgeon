
first_pick = input('Enter a card ')
second_pick = input('Enter a card ')
third_pick = input('Enter a card ')

user_list = [first_pick, second_pick, third_pick]

deck = {
    'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'j': 10, 'Q': 10, 'K': 10

}

sum_of_cards = []

for card in user_list:
    sum_of_cards.append(deck[card])

total = sum(sum_of_cards)


def helper(total):
    if total <= 16:
        return "Hit"
    elif total >= 17 or 20:
        return 'Stay'
    elif total == 21:
        return 'Blackjack'


print(helper(total))
