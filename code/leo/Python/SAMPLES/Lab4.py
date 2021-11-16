
first_word = input('Enter the first word: ')
second_word = input('Enter the second word: ')

list_first_word = list(first_word.lower().strip())
list_second_word = list(second_word.lower().strip())

list_first_word.sort()
list_second_word.sort()

if list_first_word == list_second_word:
    print(f"{first_word} and {second_word} are anagrams")

else :
    print(f"{first_word} and {second_word} are 'NOT' anagrams")