#Lab 9: Compute Automated Readability Index
#use ceil to round up
import math
import time

print("")
welcome_message = "Welcome to the Library-Interface's ARI Calculator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.04)
print("")
time.sleep(.7)
message_wait = "Reading book, calculating score..."
for char in message_wait:
  print(char, end='', flush=True)
  time.sleep(.04)
time.sleep(1)
print("")
print("")

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

#insert the text file here and all the rest is automated
book = 'gettysburgAddress.txt'

def ari_score(book):
    with open(book, 'r') as f:
        contents = f.read()
    sentence_attempt = contents.count('.') + contents.count('!') + contents.count('?')
    not_sentence = contents.count('. . .') * 3 #There are 3 dots in each, but need to times 3 to git rid of them
    sentence = sentence_attempt - not_sentence #get rid of ... in speech
    words = len(contents.split(" "))
    remove_spaces = contents.replace(" ","")
    characters = len(remove_spaces)

    print("Sentences: ", sentence)
    time.sleep(.4)
    print("Words: ", words)
    time.sleep(.4)
    print("Characters: ", characters)
    time.sleep(1)

    ARI = math.ceil(4.71 * (characters/words) + 0.5 * (words/sentence) -21.43)
    ari_results = ari_scale[ARI]
    print(f"{book.replace('.txt', '')} has an ARI score of {ARI} and is suitable for ages {ari_results['ages']} or students in the {ari_results['grade_level']}")

ari_score(book)