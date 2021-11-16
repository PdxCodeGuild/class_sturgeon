# pick6

import random

# generates a ticket with 6 numbers
def pick6 ():
    return [random.randint(1,99) for x in range(6)]


# checks to see how many matching numbers there are
def num_matches (winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
    return matches


# what you win based on number of matches
def winnings (num_matches):
    if num_matches == 1:
        return 4
    elif num_matches == 2:
        return 7
    elif num_matches == 3:
        return 100
    elif num_matches == 4:
        return 50000
    elif num_matches == 5:
        return 1000000
    elif num_matches == 6:
        return 25000000
    else:
        return 0
        

total_winnings = 0
ticket_cost = 0

winning_ticket = pick6()

# creates x number of tickets, checks the matches with the winning ticket, sums the winnings and sums the ticket cost
for _ in range(100000):
    ticket = pick6()
    matches = num_matches(winning_ticket, ticket)
    total_winnings += winnings(matches)
    ticket_cost += 2


final_balance = total_winnings - ticket_cost
print(f'You won ${total_winnings} and spent ${ticket_cost} on Pick6.\nYour final balance is ${final_balance}')


roi = final_balance / ticket_cost
print(f'Your return on investment is ${roi}')