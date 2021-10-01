

class Player:
    def __init__(self, player, token):
        self.name = player
        self.token = token


class Game:
    def __init__(self):
        self.board = [' ' for x in range(10)]

    def __repr__(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])

    def move(self, token):
        move = int(input(f'Choose a postion to place {token} (1-9) '))
        self.board[move] = token
        return self.board

    def calc_winner(self, token):
        return (self.board[1] == token and self.board[2] == token and self.board[3] == token or
                self.board[4] == token and self.board[5] == token and self.board[6] == token or
                self.board[7] == token and self.board[8] == token and self.board[9] == token or
                #---------------------------------------Going down---------------------------------#
                self.board[1] == token and self.board[4] == token and self.board[6] == token or
                self.board[2] == token and self.board[5] == token and self.board[8] == token or
                self.board[3] == token and self.board[6] == token and self.board[9] == token or
                #---------------------------------------Going across--------------------------------#
                self.board[1] == token and self.board[5] == token and self.board[9] == token or
                self.board[7] == token and self.board[5] == token and self.board[3] == token or
                self.board[3] == token and self.board[5] == token and self.board[7] == token or
                self.board[9] == token and self.board[5] == token and self.board[1] == token)

    def is_board_full(self):
        if self.board.count(' ') > 1:
            return False
        else:
            return True

    def is_game_over(self, token):
        if self.is_board_full() or self.calc_winner(token):
            return True


name1 = input("Type in your name ")
token1 = input("Choose your token x or o:  ")

name2 = input("Type in your name ")
token2 = input("Choose your token x or o:  ")

player1 = Player(name1, token1)
player2 = Player(name2, token2)

print("Welcome to Tik Tak Toe: ")

game = Game()
while True:
    game.__repr__()
    game.move(token1)
    if game.is_game_over(token1):
        break
    game.__repr__()
    game.move(token2)
    game.__repr__()
    if game.is_game_over(token1):
        break

game.__repr__()
if game.calc_winner(token1):
    print(f'{name1} you win! ')
elif game.calc_winner(token2):
    print(f'{name2} you win! ')
if game.is_board_full():
    print('Gamebaord is full. It\'s a tie!')
