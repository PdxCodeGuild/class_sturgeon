#ARI
characters = 0

with open('sampletxt.txt') as f:
    contents = f.read()
    print(contents)

# count characters
for x in contents:
    characters += 1
print(f'characters - {characters}')

# count words
words = contents.split()
number_of_words = len(words)
print(f'Words - {number_of_words}')

# count sentences
lines = contents.split('.')
number_of_lines = len(lines) -1
print(f'Lines - {number_of_lines} ')

w = float(number_of_words)
l = float(number_of_lines)
c = float(characters)

api = (4.71*(c/w)) + (0.5*(w/l)) - 21.43

print(api)
print(api%1)
if 0 < (api % 1) > 1:
    api -= api - (api % 1) + 1
print(api)