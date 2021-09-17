# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if a % 2 == 0:
        a == True
        return "even"
    if a % 2 == 1:
        a == False
        return "odd"
    else:
        print("This is not a valid entry, input a number")

check5 = is_even(5)
check6 = is_even(6)
print('Given number is', check5) #Comes out odd
print('Given number is', check6) #Comes out even

#Alternate method using bitwise-and operator
def is_it_odd(n):
    return "odd" if n&1 else "even"

print(f'Is it odd says 5 is: {is_it_odd(5)}')
print(f'Is it odd says 6 is: {is_it_odd(6)}')

#built in test that visual studio code hates
def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True
    


# Ones Digit
# Write a function that returns the ones digit of a number

# def ones_digit(num):
#     ...

# def test_ones_digit():
#     assert ones_digit(3) == 3
#     assert ones_digit(56) == 6
#     assert ones_digit(812) == 2


# # Percentage
# # Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

# def percentage(v, max):
#     ...

# def test_precentage():
#     assert percentage(1, 10) == '10%'
#     assert percentage(600, 1200) == '50%'
#     assert percentage(1, 3) == '33%'
