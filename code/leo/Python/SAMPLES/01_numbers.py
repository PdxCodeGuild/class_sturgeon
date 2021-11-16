# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if (a % 2) == 0:
        return True
    else:
        return False

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    num = str(num)

    return num[-1]

# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):

    return (f'{int((v / max) * 100)}%')

