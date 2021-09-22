#ARI
import re

# Open file
with open('gettysburg_address.txt', 'r') as f:
    contents = f.read()
    

# count characters except spaces
characters = 0
for x in contents:
    if x == ' ':
        continue
    else:
        characters += 1
print(f'characters - {characters}')

# count words
words = re.split(' ', contents)
number_of_words = len(words)
print(f'Words - {number_of_words}')

# count sentences
sentences = re.split('[.?!]', contents)
number_of_sentences = len(sentences) -1
print(f'Sentences - {number_of_sentences} ')

# convert varialbes to floats
w = float(number_of_words)
s = float(number_of_sentences)
c = float(characters)

#calculate api
ari = (4.71*(c/w)) + (0.5*(w/s)) - 21.43

#round up any float
if ari%1 > 0:
    ari = (ari//1) + 1
    print(f'ARI = {ari}')
else:
    print(f'ARI = {ari}')

ari = int(ari)

# ari scale dict
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print(f'''
-----------------------------------------------------------
The ARI for {f.name} is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person of {ari_scale[ari]['ages']} years old.
-----------------------------------------------------------
''')