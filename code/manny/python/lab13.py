import sys

#main function
def main_game():
    player_one_name = input("Player one, what is your name? ")
    player_one_token = input("Would you like to be represented by X or O? ")
    player_one_token = player_one_token.upper()
    valid_tokens = ["Y", "O"]
    if player_one_token not in valid_tokens:
        print("Please select a valid variable the next time you play.")
        sys.exit()
    valid_tokens.remove(player_one_token)
    player_two_name = input("Player two, what is your name? ")
    player_two_token = valid_tokens[0]

    print(f"{player_one_name} your token for this game will be {player_one_token}")
    print(f"{player_two_name} your token for this game will be {player_two_token}")

main_game()


class Player:    
    def __init__(self, name, token):
        player_one_name = input("Player one, what is your name? ")
        player_one_token = input("Would you like to be represented by the letter X or O? ")
        player_one_token = player_one_token.upper()
        valid_tokens = ["Y", "O"]
        if player_one_token not in valid_tokens:
            print("Please select a valid variable the next time you play.")
            sys.exit()
        valid_tokens.remove(player_one_token)
        player_two_name = input("Player two, what is your name? ")
        player_two_token = valid_tokens[0]



        print(f"{player_one_name} your token for this game will be {player_one_token}")
        print(f"{player_two_name} your token for this game will be {player_two_token}")


class Game:    
    def __repr__(self, board):
        board.self = board
        row_1 =  {[],[],[]}
        row_2 =  {[],[],[]}
        row_3 =  {[],[],[]}
        
        board = row_1 + "\n" + row_2 + "\n" + row_3

        print(board)

    def move(x,y,player):     
        pass 

    def calc_winner():
        pass

    def is_full():
        pass

    def is_game_over():
        pass 
    
#main function
def main_game():
    player_one_name = input("Player one, what is your name? ")
    player_one_token = input("Would you like to be represented by X or Y? ")
    player_one_token = player_one_token.upper()
    valid_tokens = ["Y", "X"]
    if player_one_token not in valid_tokens:
        print("Please select a valid variable the next time you play.")
        sys.exit()
    valid_tokens.remove(player_one_token)
    player_two_name = input("Player two, what is your name? ")
    player_two_token = valid_tokens[0]

    print(f"{player_one_name} your token for this game will be {player_one_token}")
    print(f"{player_two_name} your token for this game will be {player_two_token}")

main_game()
