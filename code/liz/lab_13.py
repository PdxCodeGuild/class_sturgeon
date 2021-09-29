# tic-tac-toe


class Player:
    def __init__ (self, t, n):
        self.n = n
        self.t = t


class Game:
    def __init__ (self):
        self.b = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    
    def __repr__(self):
        for i in self.b:
            return '|'.join(i)
    
    def move (self, x, y, player):
        self.b[y][x] = player.t

    #def calc_winner (self):
  
    
    def is_full (self):
        for i in self.b:
            for j in i:
                if j == ' ':
                    return False
        return True






print('Welcome to Tic-Tac-Toe!')
while True:
    game = Game()
    command = input("Would you like to play a game? 'yes' or 'no': ")
    if command == 'yes':
        name1 = input("Enter player 1's name: ")
        token1 = input("What token would you like? 'X' or 'O': ")
        name2 = input("Enter player 2's name: ")
        if token1 == 'X':
            token2 = 'O'
        else:
            token2 = 'X'
        player1 = Player(name1, token1)
        player2 = Player(name2, token2)
# get players to alternate turns
# check and print out gameboard


    elif command == 'no':
        break
    else:
        print('Entry not recognized')

    

#game.__repr__()