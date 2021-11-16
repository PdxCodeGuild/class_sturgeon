'''
Let's play rock-paper-scissors with the computer.

Greet the user and use a for loop to display their possible choices.
Welcome to Rock, Paper, Scissors!

Your options are:

- Rock
- Paper
- Scissors

Enter your selection:  
The computer will ask the user for their choice (rock, paper, scissors).
The computer will randomly choose rock, paper or scissors.
Compare the players' choices and determine who won and tell the user.
'''


import random

options = ['rock','paper','scissors']

print('''
Welcome to Rock, Paper, Scissors!

Your options are:
''')
for option in options:
    print(f" - {option}")

player1 = input('''
Enter your selection: ''')

player = player1.lower()

computer = random.choice(options)

if player == computer :
    print(f" Computer chooses {computer} and you choose {player1}. Its a Tie")

elif player == "rock" :
    if computer == "paper" :
        print(f" Computer chooses {computer} and you choose {player1}. You Lose -_-")
    elif computer == "scissors" :
        print(f" Computer chooses {computer} and you choose {player1}. You Win!!!")

elif player == "paper" :
    if computer == "scissors" :
        print(f" Computer chooses {computer} and you choose {player1}. You Lose -_-")
    elif computer == "rock" :
        print(f" Computer chooses {computer} and you choose {player1}. You Win!!!")

elif player == "scissors" :
    if computer == "rock" :
        print(f" Computer chooses {computer} and you choose {player1}. You Lose -_-")
    elif computer == "paper" :
        print(f" Computer chooses {computer} and you choose {player1}. You Win!!!")

