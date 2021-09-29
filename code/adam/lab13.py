# Lab 13: Tic-Tac-Toe
import time

class Player:
    def __init__(self, name, token):  #We'll ask each player to enter their name and token (x or o)
        self.name = name
        self.token = token

class Game:
    def __init__(self):   #This dictionary is what we'll call on for key and value for the game
        self.board = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}

    def __repr__(self, board): #Returns a pretty string representation of the game board
        print('    The Current Board          Positions')
        print('  ', board['1'], '  |','  ' ,board['2'], '  |', '  ',board['3'], '        1 | 2 | 3')
        print('-------+--------+--------')
        print('  ', board['4'], '  |','  ' ,board['5'], '  |', '  ',board['6'], '        4 | 5 | 6')
        print('-------+--------+--------')
        print('  ', board['7'], '  |','  ' ,board['8'], '  |', '  ',board['9'], '        7 | 8 | 9', '\n')

    def move(self, x, y, player): #Didn't really end up using this as the coordinate system seemed more difficult than the dictionary + pretty picture
        x = int(input(f"What is player {player}'s x position?"))
        y = int(input(f"What is player {player}'s y position?"))
    
    def calc_winner(self, board):
        check = ' '
        if board['1'] == board['2'] == board['3'] != ' ' : #row 1
           check = "win"
        elif board['4'] == board['5'] == board['6'] != ' ': #row 2
           check = "win"
        elif board['7'] == board['8'] == board['9'] != ' ': #row 3
           check = "win"
        elif board['1'] == board['4'] == board['7'] != ' ': #column 1
           check = "win"
        elif board['2'] == board['5'] == board['8'] != ' ': #column 2
           check = "win"
        elif board['3'] == board['6'] == board['9'] != ' ': #column 3
           check = "win"
        elif board['7'] == board['5'] == board['3'] != ' ': #diagnal forward slash
           check = "win"
        elif board['1'] == board['5'] == board['9'] != ' ': #diagnal backslash
          check = "win"
        return check
    
    def is_full(self, board):
        if ' ' not in board.values():  #Default is for a space is ' ', so anything else means all slots are full
            print("Game is a tie")
    
    def is_game_over(self):  #Another one that I didn't end up using
        self.is_full()
        self.calc_winner()

print("\t--------------------------------")
print("\t         Tic Tac Toe            ")
print("\t--------------------------------")

print("")
welcome_message = "Welcome to the Library-Interface's Tic Tac Toe"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.04)
print("")

while True: #Asking for Player 1 details using the Player class, and ensuring the input is logical
    player1_name = input("Enter name for Player 1:-->")
    player1_token = input("What is your choice of token (X or O)?:-->").upper()
    if player1_token != "X" and player1_token != "O":
        print("You need to enter an X or O for token")
        continue
    break
while True: #Asking for Player 2 name using the Player class & ensuring it's not the same as player 1
    player2_name = input("Enter name for Player 2:-->").upper()
    if player2_name == player1_name:
        print("No, enter your name")
        continue
    break
while True: #Asking for Player 2 token, ensuring it's unique
    if player1_token == "X":
        player2_token = "O"
        print(f"{player2_name}, You are 'O' by default")
    elif player1_token == "O":
        player2_token = "X"
        print(f"{player2_name}, You are 'X' by default")
    break

player1 = Player(player1_name, player1_token)
player2 = Player(player2_name, player2_token)
time.sleep(1.4)
print("")

game = Game()  #making the Game() easier to type inside of the play_game()

def play_game():
    current_player = player1 #Starting off with player 1 every game
    for i in range(9): #There are only 9 spots in a tic tac toe game
        game.__repr__(game.board)
        print(f"It is {current_player.name}'s turn to play. Choose a Square for {current_player.token}: \n")
        while True:
            user_choice = input()
            if user_choice in [str(x) for x in range(1, 10)]: #This makes a string list to look inside of for correct user input ie ["1", "2"]
                break
            print("Not a valid choice, choose from Positions:")
        while True:
            if game.board[user_choice] == ' ': #If user picks key 7, it checks to see if 7 is available
                game.board[user_choice] = current_player.token #If available, game secures the key and adds the value
                break
            else:
                if game.board[user_choice] == "X":
                    print(f"Player 1: already played that move, place your {current_player.token} elsewhere\n")
                else:
                    print(f"Player 2: already played that move, place your {current_player.token} elsewhere\n")
                game.__repr__(game.board)
                user_choice = input()
        check = game.calc_winner(game.board)
        if check == "win":  #A more dramatic version of announcing the winner
            winner = 'The winner is:', '... ... ... ', '... ... ... ', current_player.name, "!"
            for char in winner:
                print(char, end='', flush=True)
                time.sleep(1)
            print("")
            break
        else:
            game.is_full(game.board) #This checks to see if the board is full for a tie, but doesn't show up if someone wins
        if current_player == player1: #this if/else forces it to change turns each iteration
            current_player = player2
        else:
            current_player = player1
    print("")
    again = input("Thanks for playing. Would you like to play again? (y or n):-->").lower()
    if again == "y":
        for key in game.board:   #This resets the board so that you can play again
            game.board[key] = ' '
        play_game()

play_game()