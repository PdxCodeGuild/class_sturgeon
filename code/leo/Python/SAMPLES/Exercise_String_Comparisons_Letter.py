'''
Assign a letter to a variable to serve as the secret answer

Ask the user to enter a letter, assign it to a variable

if the user's letter is the same as the answer, inform the user they've guessed correctly. 
Otherwise, inform them they've erred and display the correct answer.

'''


answer = "A"

letter = input('Enter a letter: ')

letter = letter.upper()

if answer == letter :
    print(f'Great Job!!! The secret letter is {answer} and you answered {letter} :) !!!')

elif answer != letter :
    print(f'Ohh no!!! The secret letter is {answer} and you answered {letter} :( !!!')