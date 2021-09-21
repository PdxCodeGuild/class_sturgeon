import random
counter = 0
balance = 0
expenses = 0
earnings = 0

def pick6():
    num_list = []
    num_list.append(random.randint(1, 99))
    num_list.append(random.randint(1, 99))
    num_list.append(random.randint(1, 99))
    num_list.append(random.randint(1, 99))
    num_list.append(random.randint(1, 99))
    num_list.append(random.randint(1, 99))
    return num_list
# return [ random.randint(1,99) for x in range(6)] = list comprehension

def num_matches(winning, ticket):
    matches = 0
    if winning[0] == ticket[0]:
        matches += 1
    if winning[1] == ticket[1]:
        matches += 1
    if winning[2] == ticket[2]:
        matches += 1
    if winning[3] == ticket[3]:
        matches += 1
    if winning[4] == ticket[4]:
        matches += 1
    if winning[5] == ticket[5]:
        matches += 1
    return matches
''' def num_matches(winning, ticket):
    for i in range(len(winning_ticket)):
        if winning[i] == ticket[i]:
            matches += 1
        return matches
'''
'''
creates tuples to compare 2 lists
list1 = []
list2 = []
print(list(zip(list1, list2)))
'''
winning_numbers = pick6()


while counter < 100000:
    ticket_numbers = []
    counter += 1
    balance -= 2
    expenses += 2


    ticket_numbers = pick6()

    matches = num_matches(winning_numbers, ticket_numbers)

    if matches == 6:
        balance += 25000000
        earnings += 25000000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 1:
        balance += 4
        earnings += 4
# could simplify above with dict instead of if statements
# dict is outside of loop
roi = (earnings - expenses)/expenses   

print(f'Final Balance = ${balance}')
print(f'Expenses = ${expenses}')
print(f'Earnings = ${earnings}')
print(f'ROI = {roi}')