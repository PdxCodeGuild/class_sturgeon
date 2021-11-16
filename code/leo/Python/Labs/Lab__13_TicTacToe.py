class Player:      # Creates Players and Tokens
    def __init__(self):
        self.name = input('Enter player name: ').title()  
        self.token = input('Choose X or O: ').upper()


class Game:
    def __init__(self): #Create a game board
        self.gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def __repr__(self): # Visual representation of a game board
    
        return f'''
                    {self.gameboard[0][0]} | {self.gameboard[0][1]} | {self.gameboard[0][2]}
                    --|---|--
                    {self.gameboard[1][0]} | {self.gameboard[1][1]} | {self.gameboard[1][2]}
                    --|---|--
                    {self.gameboard[2][0]} | {self.gameboard[2][1]} | {self.gameboard[2][2]}
                '''

    def move(self, player):   #asks player for a x and y position and add players token to the board
        x = int(input(f'''
                            Enter the horizontal "x" position
                            x0 y0 | x1 y0 | x2 y0
                            x0 y1 | x1 y1 | x2 y1
                            x0 y2 | x1 y2 | x2 y2
                            >>>> '''))
            
        y = int(input(f'''
                            Enter the vertical "y" position
                            x0 y0 | x1 y0 | x2 y0
                            x0 y1 | x1 y1 | x2 y1
                            x0 y2 | x1 y2 | x2 y2
                            >>>> '''))

        self.gameboard[y][x] = player.token

        return self.gameboard

    def calc_winner(self): # if and elif if board have a winner, returns True if winner and False if no winner

        if self.gameboard[0][0] == self.gameboard[0][1] == self.gameboard[0][2] != " " or self.gameboard[1][0] == self.gameboard[1][1] == self.gameboard[1][2] != " " or self.gameboard[2][0] == self.gameboard[2][1] == self.gameboard[2][2]!= " ":
            return True
        elif self.gameboard[0][0] == self.gameboard[1][0] == self.gameboard[2][0] != " " or self.gameboard[0][1] == self.gameboard[1][1] == self.gameboard[2][1] != " " or self.gameboard[0][2] == self.gameboard[1][2] == self.gameboard[2][2] != " ":
            return True
        elif self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] != " " or self.gameboard[2][0] == self.gameboard[1][1] == self.gameboard[0][2] != " ":
            return True

        else:
            return False

    def is_full(self):    # return True if game full and False if not full
        thereturn = True
        for inside in self.gameboard:
            if " " in inside:
                thereturn = False
        return thereturn

    def is_game_over(self): # for the while loop - True is game full or winner
        if self.calc_winner == True or self.is_full == True:
            return True
        else:
            return False


#here is where the game starts   
player1 = Player() #choose player 1
print(f'\n First player is " {player1.name} ", and {player1.name} will be playing with " {player1.token} ".\n') #print player1
player2 = Player() #choose player 2
print(f'\n Second player is " {player2.name} ", and {player2.name} will be playing with " {player2.token} ".\n') #print player2
board = Game() #create a boar

while board.is_game_over() == False:    #will run until board full or winner are True
    
    print(f"It is {player1.name}'s turn") # tells player 1 turn
    board.move(player1)                 # player1 makes move
    print(board)                        # print board with player 1's move
    
    if board.is_full():                 # check if board is full
        print('Game is full')         
        break                           # break loop returning True to while loop
    elif board.calc_winner():           # check if player 1 is a winner
        print(f'{player1.name} you are the winner!!!')
        break                           # break loop returning True to while loop
    
    else:                               # if game not full or player 1 is a winner - player 2 plays
        print(f"It is {player2.name}'s turn") 
        board.move(player2)
        print(board)
        if board.calc_winner():         # check if player 2 is a winner
            print(f'{player2.name} you are the winner!!!')
            break                       # break loop returning True to while loop
        else:
            continue


print('\nThanks for playing!!!\n')
