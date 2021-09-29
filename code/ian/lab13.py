
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


    
game = Game()

print('Welcome to Tic Tac Toe!')

p1 = Player(input('Player 1 name: '), input('X or O?: '))

p2 = Player(input('Player 2 name: '), 'O' if p1.token == 'X' else 'X')

print(f'{p1.name} is {p1.token}\'s')
print(f'{p2.name} is {p2.token}\'s\n')


print(game)

game.move( int(input('How many spaces to the right? 0-2: ')), int(input('How many spaces down? 0-2: ')), p1)
print('next turn')

print(game)