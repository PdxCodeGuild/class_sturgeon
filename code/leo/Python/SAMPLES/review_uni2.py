
'''
# loop - a code block that repeats until a certain condition is met
​
# for item in sequence - loop through each item in the sequence
​
# for/in - Python operators
# item - arbitrary variable name to store each item as the loop visits it
# sequence - string, list or other 'iterable' (loopable) object
'''
for color in colors:
    print(color)
'''
# -------------------------------------------------------------------------------------------- #
​
numbers = [2, 4, 6]
​
numbers_squared = []
​
for number in numbers:
    # square the number and add it to the list
    numbers_squared.append(number ** 2)
​
# print(numbers_squared)
​
# ---------------------------------------------------------------------------------------------- # 
# for x in range() - loop a certiain number of times
​
# range(stop) - return a range of numbers from 0 to stop-1
# print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
​
​
powers_of_2 = []
for number in range(11):
    powers_of_2.append(2 ** number)
​
# print(powers_of_2) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
​
# range(start, stop, step)
'''
for x in range(0, 101, 10):
    print(x)
'''
# -------------------------------------------------------------------------------------- #
​
# while loop
​
'''
while some_condition == True:
    # loop this
    # code block
'''
​
# "for x in range(10)" with a while loop
​
x = 0
​
while x < 10:
    # print(x)
​
    x += 1
​
# -------------------------------------------------------------------------------------- #
​
# loop controls
# continue, break, else
​
for x in range(10):
​
    if x == 8:
        print('goodbye')
        break # end the loop immediately
​
    elif x == 3:
        print('...')
        continue # skip the rest of this iteration and begin the next
​
    print(x)
​
else:
    # else will be run if the loop makes it all the way through =
    # i.e. if its condition becomes False
    print("The loop ran all the way through")