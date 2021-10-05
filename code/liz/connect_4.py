# connect four

class Player:
    def __init__ (self, n, c):
        self.n = n
        self.c = c
    
    def __repr__ (self):
        return self.n

class Game:
    def __init__ (self):
        self.b = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
    
    def __repr__ (self):
        for i in self.b:
            print('|', '|'.join(i), '|')
    
    def get_height (self, position):
        counter = -6
        for i in self.b:
            counter += 2
            for j in i:
                if j != ' ':
                    return self.b[i] + counter

    #def move (self, player, position):

game = Game()

game.__repr__()
