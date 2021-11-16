'''
2.1
Use string methods to determine the number of times a letter occurs in a word

Output

word: bookkeeper
letter: k

output: 2
The letter 'k' occurs in the word 'bookkeeper' 2 times.
2.2
Ask the user for a word
Ask the user for a letter
Assign the word and the letter to variables
Determine how many times the letter occurs in the word
Output

Enter a word: hippopotamus
Enter a letter to count: p

Output:
The letter 'p' occurs 3 times in 'hippopotamus'

'''


word = input('Enter a word: ')
letter = input('Enter a letter: ')

times = word.count(letter)
print(f'The letter {letter} occurs {times} in the word {word}')
