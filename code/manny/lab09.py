import re
import math 

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

with open('gettysburg.txt', 'r') as f:
    contents = f.read()

def num_sentences(speech):
    sentences = re.split("[.!?]", speech)
    return len(sentences)

def num_words(speech):
    words = re.split(r" ", speech)
    return len(words)

def num_characters(speech):
    characters = re.findall("[A-Za-z]", speech)
    return len(characters)

characters = num_characters(contents)
words = num_words(contents)
sentences = num_sentences(contents)

ari_score = 4.71*(characters/words)+0.5*(words/sentences)-21.43

give_score = math.ceil(ari_score)

ari_details = ari_scale[give_score]

#print(f"The ARI for gettysburg-address.txt is {give_score}")
#print(f"This corresponds to a {ari_details[1]} Grade level of difficulty")
#print(f"that is suitable for an average person {ari_details[2]} years old.")