#LCR Left Center Right Game

import random
import time

class Player:
    def __init__(self, name, cash): 
        self.name = name
        self.cash = cash
    def __repr__(self): #Represenaton of what you want to see when you print Player
        return (f'{self.name}, has ${cash}')

players = []

#Ulitmately didn't go this route as I wanted more to happen in the function
def roll_LCR(num_dice):
    #Roll the dice and return a list of n strings
    output = []
    for i in range(num_dice):
        roll = random.choice(["L", "C", "R", "O", "O", "O"])
        output.append(roll)

def roll_dice(current_player, player_money, player_count):
    dice = random.randint(1,6)
    if dice == 1:
        die = '\tLeft'
        player_money[current_player] -= 1
        player_money[(current_player + 1) % player_count] += 1 #the % player_count keeps index from going out of range
    if dice == 2:
        die = '\tCenter'
        player_money[current_player] -= 1 
        player_money[current_player - 1] += 1
    if dice == 3:
        die = '\tRight'
        player_money[current_player] -= 1 
    if dice > 3:
        die = '\tDot'
    print(die)
    return player_money

def roll(masterlist, current_player):
    dice = random.randint(1,6)
    index = masterlist.index(current_player)
    if dice == 1:
        die = '\tLeft'
        current_player.cash -= 1
        masterlist[((index -1) % len(masterlist))].cash += 1
    if dice == 2:
        die = '\tRight'
        current_player.cash -= 1
        masterlist[((index +1) % len(masterlist))].cash += 1
    if dice == 3:
        die = '\tCenter'
        current_player.cash -= 1 
    if dice > 3:
        die = '\tDot'
    print(die)

print("\t--------------------------------")
print("\t         Left Center Right      ")
print("\t--------------------------------")

print("")
welcome_message = "Welcome to the Library-Interface's Left Center Right"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.04)
print("")

num_players = input("How many players? (Minimum of 3)\n")

for player_count in range(int(num_players)):
    name = input(f"Enter Player {player_count + 1}'s name:-->").title()
    cash = int(input(f"How much cash did {name} show up with today?:-->"))
    players.append(Player(name, cash))

print("\nAll players prepare for LCR\n")

def LCR(players):
    while True:
        for person in players:
            #elifs to determine how many rolls
            if person.cash <= 0:
                print(f"{person.name} is broke, skip")
            elif person.cash >= 3:
                print(f"{person.name} gets to roll 3 dice with ${person.cash}")
                for roll_count in range(3):
                    time.sleep(.5)
                    roll(players, person)
            elif person.cash == 2:
                print(f"{person.name} gets to roll 2 dice with $2")
                for roll_count in range(person.cash):
                    time.sleep(.5)
                    roll(players, person)
            elif person.cash == 1:
                print(f"{person.name} gets to roll 1 die with $1")
                for roll_count in range(person.cash):
                    time.sleep(.5)
                    roll(players, person)
        eligible_players = [person for person in players if person.cash > 0]
        if len(eligible_players) == 1:
            return eligible_players
        if len(eligible_players) == 0:
            return None

while True:
    winning_player = LCR(players)
    if winning_player == None:
        print("Everyone died when a meteor crashed into the building")
    else:
        print(f'Congrats to {winning_player} for winning LCR!')
    if input("Would everyone like to buy in again for $5? (y or n)") != 'y':
        break
    for player in players:
        player.cash = 5
