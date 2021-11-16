# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather

def go_hiking(weather):
    if weather == 'rainy':
        return "don't go hiking"
    elif weather == 'sunny':
        return "yes, go hiking, but make sure you hydrate"
    else:
        return "idk brohhh, your called"

# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    if len(str(abs(num))) == 2:
        return True
    else:
        return False

# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    
    if abs(a) == a and abs(b) == b:
        return False

    elif abs(a) != a and abs(b) != b:
        return False

    elif abs(a) == a and abs(b) != b:
        return True
    
    elif abs(a) != a and abs(b) == b:
        return True

# Near 100
# Write a function that returns True if a number within 10 of 100.

def near_100(num):

    if num <= 100 and num >= 10:
        return True
    else:
        return False

# Maximum of Three
# Write a function that returns the maximum of 3 parameters.

def maximum_of_three(a, b, c):

    return max(a, b, c)

