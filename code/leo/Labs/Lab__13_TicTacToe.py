
def player():
    name = input('Enter player name: ').title()
    token = input('Choose X or O: ').upper()

    return [name, token]

def game():
    gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return gameboard
    
def print_game(gameboard):     
    
    return f'''
                    {gameboard[0][0]} | {gameboard[0][1]} | {gameboard[0][2]}
                    --|---|--
                    {gameboard[1][0]} | {gameboard[1][1]} | {gameboard[1][2]}
                    --|---|--
                    {gameboard[2][0]} | {gameboard[2][1]} | {gameboard[2][2]}
            '''
    
def move(gameboard, token):  
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
    

    gameboard[x][y] = token[1]

    return gameboard

def calc_winner(gameboard):

    if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] != " " or gameboard[1][0] == gameboard[1][1] == gameboard[1][2] != " " or gameboard[2][0] == gameboard[2][1] == gameboard[2][2]!= " ":
        return True
    elif gameboard[0][0] == gameboard[1][0] == gameboard[2][0] != " " or gameboard[0][1] == gameboard[1][1] == gameboard[2][1] != " " or gameboard[0][2] == gameboard[1][2] == gameboard[2][2] != " ":
        return True
    elif gameboard[0][0] == gameboard[1][1] == gameboard[2][2] != " " or gameboard[2][0] == gameboard[1][1] == gameboard[0][2] != " ":
        return True

    else:
        return False

def is_full(gameboard):
    thereturn = True
    for inside in gameboard:
        if " " in inside:
            thereturn = False
    return thereturn

def is_game_over(gameboard):
    if calc_winner == True or is_full == True:
        return True
    else:
        return False
    
player1 = player()
player2 = player()
board = game()

print(print_game(board))
move(board, player1)
move(board, player2)
print(print_game(board))

