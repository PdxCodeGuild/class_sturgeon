import random

def pick6(): #Generates a list with 6 random numbers from 1 - 99
    ticket = []
    for x in range(6):
        y = random.randint(1,99)
        ticket.append(y)

    return(ticket)

def num_matches(winning, ticket): #Matches two tickets and return number of matches
    match = 0
    index = 0
    while index < 6:
        if winning[index] == ticket[index]:
            match += 1
            index += 1
        else:
            index += 1
    return match

cost = 0
earn = 0
result = 0
winning = pick6() #generate 6 random winning numbers

for x in range(100000): #run the loop 100 thousand time adding to cost and earning
    cost = cost + 2 #adding $2 each loop
    ticket = pick6() #generate a new random ticket each loop
    result = num_matches(winning, ticket) # result for each match

    if result == 1:    # add winning $ 
        earn = earn + 4
    elif result == 2:
        earn = earn + 7
    elif result == 3:
        earn = earn + 100
    elif result == 4:
        earn = earn + 50000
    elif result == 5:
        earn = earn + 1000000
    elif result == 6:
        earn = earn + 25000000

if earn < cost:
   print(f'''
   Ohh NO!!! 
   You expended a total of ${cost} in tickets, and you only won ${earn}
   Now you are negative ${cost - earn} bucks ... 
   
   You ROI is on the negative {(earn - cost) / cost} 
   
   ...you shouldnt played in the lotto one hundred thousand times -__-

   ''')

else:
   print(f'''
   Congradulation!!! 
   You expended a total of ${cost} in tickets, but you won ${earn} bucks!!!!
   Now you gotta ${earn - cost} bucks extra in your pocket... 

   You ROI is {(earn - cost) / cost} 

   dont forget to save the taxes !!!

   ''')
