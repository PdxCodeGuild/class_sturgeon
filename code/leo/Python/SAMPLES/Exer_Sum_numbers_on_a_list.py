import random

numbers = []
# loop ten times
for i in range(10):
    # generate random number between 1 and 10
    random_number = random.randint(1, 10)
    # add the number to the list
    numbers.append(random_number)

# Loop through the list of numbers and calculate the sum
# set the total to zero
total = 0
# loop through the numbers
for number in numbers:
    # add the number to the total
    total += number

# calculate the average
average = total / len(numbers)

# display the result
print(f'numbers: {numbers}')
print(f'average: {average}')
    