# tic-tac-toe


class Player:
    def __init__ (self, n, t):
        self.n = n
        self.t = t
    
    def __repr__ (self):
        return self.n


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

def valid_token ():
    while True:
        token1 = input("What token would you like? 'X' or 'O': ").upper()
        if token1 == 'X' or token1 == 'O':
            return token1
        print("Not a valid token. Please enter 'X' or 'O'")

def valid_move (gb):
    terms = [
        {
            'axis' : 'column',
            'dir1' : 'left',
            'dir2' : 'middle',
            'dir3' : 'right',
        },
        {
            'axis' : 'row',
            'dir1' : 'top',
            'dir2' : 'middle',
            'dir3' : 'bottom',
        }
    ]
    
    while True:
        results = []
        for term in terms:
            while True:
                try:
                    move = int(input(f"{current_player}: What {term['axis']} would you like to place your token in?\n({term['dir1']} = 0), ({term['dir2']} = 1), ({term['dir3']} = 2)\n"))
                    
                    if move in [0, 1, 2]:
                        results.append(move)
                        break
                    print('Not a valid move. Please select 0, 1, or 2\n')
                except ValueError:
                    print('Please enter a valid number: 0, 1, or 2')
        if empty_space(results, gb):
            break
        else:
            print('This spot is taken!')
    return results

def empty_space (value_lst, gb):
    if gb.b[value_lst[0]][value_lst[1]] == ' ':
        return True
    else:
        return False




  

# start game!
print('Welcome to Tic-Tac-Toe!')

while True:
    game = Game()
    command = input("Would you like to play a game? 'yes' or 'no': ").lower()
    if command in ['yes', 'y', 'sure', 'yea', 'yep', 'yeah', 'hell yeah']:
        name1 = input("Enter player 1's name: ")
        token1 = valid_token()
        name2 = input("Enter player 2's name: ")
        token2 = 'O' if token1 == 'X' else 'X'
        player1 = Player(name1, token1)
        player2 = Player(name2, token2)


        counter = 0
        while True:
            current_player = player1 if counter % 2 == 0 else player2
            counter += 1
            move = valid_move(game)
            game.move(move[0], move[1], current_player)
            game.__repr__()
            if game.is_game_over(current_player):
                print('The game is over')
                break


        if game.is_full():
            print("Cat's game. Meow!")

        for current_player in [player1, player2]:
            if game.calc_winner(current_player):
                print(f"{game.calc_winner(current_player)}'s won the game!")


    elif command in ['no', 'n', 'nah', 'hell no', 'nope']:
        print('Goodbye!')
        break

    else:
        print('Entry not recognized')

    

# fairly ux friendly.
# need to figure out how to deal w not overriding a full space
# would like to figure out one valid move function that will check both moves
# would like to add an exit at anytime