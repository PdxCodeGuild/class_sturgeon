import random
win_list = [random.randrange(1, 99) for i in range(6)]

tick_balance = 0
winnings = 0
user_matches = 0
tickets = 100

for i in range(tickets):
    user_list = [random.randrange(1, 99) for i in range(6)]
    user_matches = 0
    tick_balance += 2
    for i in range(6):
        if user_list[i] == win_list[i]:
            user_matches += 1
    if user_matches == 1:
        winnings += 4
    elif user_matches == 2:
        winnings += 7
    elif user_matches == 3:
        winnings += 100
    elif user_matches == 4:
        winnings += 50000
    elif user_matches == 5:
        winnings += 1000000
    elif user_matches == 6:
        winnings += 25000000


print("your winnings are", winnings, "your ticket balance is", tick_balance)

'''
a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000

'''

'''
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0

Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

if user_matches == 0:
        print('no matches')
    elif user_matches == 1:
        print('one match')
    elif user_matches == 2:
        print('Two match')
    elif user_matches == 3:
        print('Three match')
    elif user_matches == 4:
        print('Four match')
    elif user_matches == 5:
        print('Five match')
    elif user_matches == 6:
        print('Six match')
    '''
