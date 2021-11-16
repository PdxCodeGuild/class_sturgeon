# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    nums = [x*2 for x in nums]
    print(nums)
    return nums

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]

# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

#Basically, make this: print("*" * int(n))
def stars(n):
    n = '*' * int(n)
    return n
   
def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    zero_over_nine = [n*0 if n > 9 else n for n in nums]
    numbers_only = [number for number in zero_over_nine if number > 0]
    return numbers_only
print(extract_less_than_ten([2, 8, 12, 18]))

def test_extract_less_than_ten():
    extract_less_than_ten([2, 8, 12, 18]) == [2, 8]