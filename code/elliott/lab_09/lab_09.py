import re
import math as m

with open('code/elliott/lab_09/gettysburg-address.txt', 'r') as f:
    contents = f.read()

words = [contents]
x = re.split(r'[.!?]+', contents)

characters = len(contents) - contents.count(' ')
words = ([i for item in words for i in item.split()])
sentences = len(x)

sum_words = 0

for w in words:
    sum_words += 1

ari = 4.71 * (characters / sum_words) + 0.5 * (sum_words / sentences) - 21.43
ari_total = m.ceil(ari)


def ari(characters, sum_words, sentences):
    ari_total = 4.71 * (characters / sum_words) + \
        0.5 * (sum_words / sentences) - 21.43
    return ari_total


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


print(f'The ARI for gettysburg-address.txt is {ari_total}')

print('This corresponds to a',
      ari_scale[ari_total]['grade_level'], 'of difficulty')

print('that is suitable for an average person',
      ari_scale[ari_total]['ages'], 'years old.')
