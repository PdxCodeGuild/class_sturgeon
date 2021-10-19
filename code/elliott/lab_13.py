

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

    def move(self):
        move = int(input("Choose a postion to place X (1-9) "))
        self.board.insert(move, 'x')
        return self.board

    # def calc_winner():

    def is_board_full(self):
        if self.board.count(' ') > 1:
            return True
        else:
            return False

    # def is_game_over():


player1 = Player("elliott", "o")
game = Game()
while True:
    print("Welcome to Tik Tak Toe: ")
    game.__repr__()
    game.move()
    game.is_board_full()
