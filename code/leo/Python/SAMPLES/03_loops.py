# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    double = []
    for x in nums:
        x *= 2
        double.append(x)

    return double

# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    start = ''
    while n > 0:
        start += '*'
        n -= 1
    
    return start

# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    
    less_than_ten = []
    for x in nums:
        if x < 10:
            less_than_ten.append(x)
        else:
            continue
    return less_than_ten

