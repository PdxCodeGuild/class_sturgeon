#Print all the number in the list that are less than or equal to 5.
numbers = [3, 3, 10, 5, 4, 5, 6, 5, 7, 2]

newlist = [x for x in numbers if x <= 5]

print(newlist)
