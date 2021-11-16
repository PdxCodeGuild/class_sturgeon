
class Player:
    def __init__(self, name, token):
        self.name = name 
        self.token = token


class Game:

    def __init__(self):

        y1 = [' ', ' ', ' ']
        y2 = [' ', ' ', ' ']
        y3 = [' ', ' ', ' ']
        board = [y1, y2, y3]
        self.board = board

    
    def __repr__(self):
        return ('\n'.join(['|'.join(i) for i in self.board]))

    
    def move(self, x, y, player):
        self.board[y][x] = player.token
        return self.board

    def calc_winner(self):
        for slice in self.board:
            if ' ' not in slice:
                if len(set(slice)) == 1:
                    return slice[0]
        for i in range(3): #verticals returning winner
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
                # both diagonals returning winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        
    def is_full(self):
        if ' ' not in self.board[0]:
            if ' ' not in self.board[1]:
                if ' ' not in self.board[2]:
                    return True
            
    def is_game_over(self):
        if self.is_full() == True:
            return True
        if self.calc_winner() == 'X':
            return True
        if self.calc_winner() == 'O':
            return True


    def turn(self, player):
        print(f"\n{player.name}'s turn")
        print(game)
        while True:
            move_x, move_y = self.verify_move()
            if self.board[move_y][move_x] == ' ':
               break 
            else:
                print('Spot taken')
        game.move(move_x, move_y, player)
        
    def verify_move(self):
        while True:
            move_x = input('\nHow many spaces to the right?: ')
            move_y = input('How many spaces down?: ')
            try:
                move_x = int(move_x)
                move_y = int(move_y)
            except:
                pass
            if move_x in [0, 1, 2] and move_y in [0, 1, 2]:
                return (move_x, move_y)
            else:
                print('Not a valid move..)')


        
        
rematch = 'y'
while rematch == 'y':
    game = Game()
    print('\nWelcome to Tic Tac Toe!')
    temp = ''
    counter = 0
    

    p1 = Player(input('Player 1 name: '), input('X or O?: '))
    while p1.token != 'X' or 'O':
        if p1.token == 'X':
            temp = 'O'
            break
        elif p1.token == 'O':
            temp = 'X'
            break
        else:
            p1.token = input("Let's try this again.. X or O?: ")
    p2 = Player(input('Player 2 name: '), temp)
    print(f'Player 1 - {p1.name} is {p1.token}\'s')
    print(f'Player 2 - {p2.name} is {p2.token}\'s\n')

    while True:
        if counter % 2 == 0:
            counter += 1
            game.turn(p1)
        elif counter % 2 == 1:
            counter += 1
            game.turn(p2)

        if game.is_full() == True:
            print('There are no winners here..')

        if game.is_game_over() == True:
            print("\nGAME OVER")
            if game.calc_winner() == p1.token:
                print(f'{p1.name.upper()} IS THE WINNER!')
                break
            elif game.calc_winner() == p2.token:
                print(f'{p2.name.upper()} IS THE WINNER!')
                break

    rematch = input('Play again? y/n..')
    if rematch == 'n':
        print('Goodbye..')
    else:
        rematch = input('Try again..')
