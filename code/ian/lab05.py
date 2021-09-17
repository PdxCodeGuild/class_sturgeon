import random
counter = 0
balance = 0

def pick6(num_list):
    number_1 = num_list.append(random.randint(1, 99))
    number_2 = num_list.append(random.randint(1, 99))
    number_3 = num_list.append(random.randint(1, 99))
    number_4 = num_list.append(random.randint(1, 99))
    number_5 = num_list.append(random.randint(1, 99))
    number_6 = num_list.append(random.randint(1, 99))

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

winning_numbers = []
pick6(winning_numbers)

while counter < 100000:
    ticket_numbers = []
    counter += 1
    balance -= 2


    pick6(ticket_numbers)

    matches = num_matches(winning_numbers, ticket_numbers)

    if matches == 6:
        balance += 25000000
    elif matches == 5:
        balance += 1000000
    elif matches == 4:
        balance += 50000
    elif matches == 3:
        balance += 100
    elif matches == 2:
        balance += 7
    elif matches == 1:
        balance += 4
        
print(f'Final Balance = ${balance}')
