'''
Ask the user for a word

Ask the user for a letter

Assign the word and the letter to variables

Use the keyword in to determine if the letter is in the word

Tell the user if the letter is in the word. Display the letter in uppercase

If the word contains the letter, tell the user how many times the letter is in the word

'''


word = input('Enter a word: ')
letter = input('Enter a letter: ')

if word.isalpha() != True  :
    print('Please enter only one word, no spaces, no number, nor characters')

elif letter in word :
    conta = word.count(letter)
    print(f'Great Job!!! The letter {letter.upper()} appears in the "{word}" {conta} times. :) !!!')

else:
    print(f'Ohh no!!! The word "{word}" does not contains the letter {letter.upper()} :( !!!')