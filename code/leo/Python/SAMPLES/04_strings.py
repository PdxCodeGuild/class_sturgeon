# Practice 4: Strings
# Copy and paste this file into your own "04_strings.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 04_strings.py"

# Loud Text
# Capitalize text and insert dashes between each letter

def loud_text(text):
 
    return '-'.join(text.upper())

# Double Letters
# Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    double = []
    for x in word:
        x = x + x
        double.append(x)

    return "".join(double)

# Count Letter
# Count the number of letter occurances in a string

def count_letter(letter, word):