import random

numbers = []

for x in range(10):
   
    random_number = random.randint(1, 10)
    
    numbers.append(random_number)

flipped = []
for number in numbers:
    flip = number * -1
    flipped.append(flip)

print(numbers)
print(flipped)

