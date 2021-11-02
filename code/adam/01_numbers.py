# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if a % 2 == 0:
        return True
    if a % 2 == 1:
        return False
    else:
        print("This is not a valid entry, input a number")

#built in test that visual studio code hates
def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True


#Alternate method using bitwise-and operator
def is_it_even(n):
    return False if n&1 else True

def test_is_it_even():
    assert is_it_even(5) == False
    assert is_it_even(6) == True

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    return num % 10

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2


# # Percentage
# # Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    fraction = v / max
    percentage = "{:.0%}".format(fraction)
    return percentage

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'
