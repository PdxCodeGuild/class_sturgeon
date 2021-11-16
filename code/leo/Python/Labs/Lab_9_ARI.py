
def count_charaters(text): #Function that counts characters in a text
    import string

    character = string.ascii_letters + string.digits + string.punctuation
    number_of_character = 0

    for x in list(text):
        if x in character:
           number_of_character += 1

    return number_of_character

def count_words(text): #Function that counts words in a text

    words_list = text.split(' ')
    number_of_words = len(words_list)

    return number_of_words

def count_sentences(text): #Function that sentences characters in a text

    number_of_sentences = text.count('!') + text.count('?') + text.count('.')

    return number_of_sentences
   
def ARI_Score(text): #Function that compute Automated Readability Index and return score
    import math

    ARI_score = math.ceil( 4.71 * (count_charaters(text) / count_words(text)) + 0.5 * (count_words(text) / count_sentences(text)) - 21.43 )

    return ARI_score

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

with open('gettysburg-address.txt', 'r') as f:
    contents = f.read()

print(f'''
--------------------------------------------------------

The ARI for gettysburg-address.txt is {ARI_Score(contents)}
This corresponds to a {ari_scale[ARI_Score(contents)]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ARI_Score(contents)]['ages']} years old.

--------------------------------------------------------
''')