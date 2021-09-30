# tic-tac-toe


class Player:
    def __init__ (self, n, t):
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
            print('|'.join(i))
    
    def move (self, x, y, player):
        self.b[y][x] = player.t

    def calc_winner (self, player):
        if self.b[0][0] == self.b[1][0] == self.b[2][0] == player.t:
            return player.t
        elif self.b[0][1] == self.b[1][1] == self.b[2][1] == player.t:
            return player.t
        elif self.b[0][2] == self.b[1][2] == self.b[2][2] == player.t:
            return player.t
        elif self.b[0][0] == self.b[0][1] == self.b[0][2] == player.t:
            return player.t
        elif self.b[1][0] == self.b[1][1] == self.b[1][2] == player.t:
            return player.t
        elif self.b[2][0] == self.b[2][1] == self.b[2][2] == player.t:
            return player.t
        elif self.b[0][0] == self.b[1][1] == self.b[2][2] == player.t:
            return player.t
        elif self.b[0][2] == self.b[1][1] == self.b[2][0] == player.t:
            return player.t
        else:
            return None
  
    
    def is_full (self):
        for i in self.b:
            for j in i:
                if j == ' ':
                    return False
        return True
    
    def is_game_over (self, player):
        full_board = self.is_full()
        someone_won = self.calc_winner(player)
        if full_board or someone_won:
            return True




# start game!
print('Welcome to Tic-Tac-Toe!')
while True:
    game = Game()
    command = input("Would you like to play a game? 'yes' or 'no': ")

    if command == 'yes':
        name1 = input("Enter player 1's name: ")
        token1 = input("What token would you like? 'X' or 'O': ").upper()
        name2 = input("Enter player 2's name: ")
        token2 = 'O' if token1 == 'X' else 'X'
        player1 = Player(name1, token1)
        player2 = Player(name2, token2)


        counter = 0
        while True:
            current_player = player1 if counter % 2 == 0 else player2
            counter += 1
            move1 = int(input('What column would you like to place your token in: 0, 1, 2? '))
            move2 =int(input('What row would you like to place your token in: 0, 1, 2? '))
            game.move(move1, move2, current_player)
            game.__repr__()
            if game.is_game_over(current_player):
                print('The game is over')
                break


        if game.is_full():
            print('The board is full!')

        for current_player in [player1, player2]:
            if game.calc_winner(current_player):
                print(f"{game.calc_winner(current_player)}'s won the game!")


    elif command == 'no':
        break
    
    else:
        print('Entry not recognized')

    

