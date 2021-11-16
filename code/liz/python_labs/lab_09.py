# compute automated readability index

import re
from math import ceil

with open('gettysburg_address.txt', 'r') as f:
    contents = f.read()

def ari (contents):

    no_ellipsis = contents.replace('. . .', ' ')
    sentences = re.split('[.?!]', no_ellipsis)
    num_sentences = len(sentences)
    # print('num_sentences: ', num_sentences)

    
    words = re.split(' ', no_ellipsis)
    num_words = len(words)
    # print('num_words: ', num_words)

    chars = re.findall(r'[a-zA-Z0-9]', no_ellipsis)
    num_chars = len(chars)
    # print('num_chars: ', num_chars)

    return ceil(4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sentences) - 21.43)

ari_score = ari(contents)
# print('ari_score: ', ari_score)

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

age_grade = ari_scale[ari_score]
#print(age_grade)

print(f'''
The ARI for {f.name} is {ari_score}
This corresponds to a {age_grade['grade_level']} level of difficulty
that is suitable for an average person {age_grade['ages']} years old.
''')