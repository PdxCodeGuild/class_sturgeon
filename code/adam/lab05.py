#Lab05: Pick6
#We don't have lottery in Utah, so this one will interesting
import random
import time

print("")
welcome_message = "Welcome to the Library-Interface's 100,000 Pick 6 Lottery Generator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
time.sleep(.5)
print("")

def generate_numbers():
    numbers = []
    count = 0
    while count < 6:
        numbers.append(random.randint(1, 99))
        count += 1
    return numbers

#Step 1: Generate a list of 6 random numbers representing the winning ticket:
winning_ticket = generate_numbers()
print("Drawing the winning lottory ticket now...")
time.sleep(1.5)
print(f"The winning ticket is: {winning_ticket}")
time.sleep(1.5)
print("Purchasing 100K lottery tickets now...")
time.sleep(1.5)
print("")

#Step 2: Start Balance at 0:
balance = 0
expenses = 0
earnings = 0

#Step 3 thru 5: loop 100,000 times, generating 6 numbered tickets and subtracting 2 from balance
i = 1

while i < 100001: #temp 11 instead of 100001 to make testing easier
    ticket = generate_numbers()
    balance -= 2
    match = 0
    print(f'{i}: \t\t$2 Pick 6 Purchased: \t{ticket}')
    if ticket[0] == winning_ticket[0]:
        match += 1
    if ticket[1] == winning_ticket[1]:
        match += 1
    if ticket[2] == winning_ticket[2]:
        match += 1
    if ticket[3] == winning_ticket[3]:
        match += 1
    if ticket[4] == winning_ticket[4]:
        match += 1
    if ticket[5] == winning_ticket[5]:
        match += 1
    if match == 0:
        match = match
    if match == 1:
        balance += 4
        earnings += 4
        print("Congrats, you win $4")
    if match == 2:
        balance += 7
        earnings += 7
        print("Congrats, you win $7")
    if match == 3:
        balance += 100
        earnings += 100
        print("Congrats, you win $100")
    if match == 4:
        balance += 50000
        earnings += 50000
        print("Congrats, you win $50k")
    if match == 5:
        balance += 1000000
        earnings += 1000000
        print("Congrats, you win $1 million!")
    if match == 6:
        balance += 25000000
        earnings += 25000000
        print("Congrats, you win $25 million!")
    match == 0
    i = i+1
    expenses += 2
print("")
print("")
ROI = (earnings - expenses)/expenses
print(f'We hope you enjoyed gambling. After spending ${expenses} and winning ${earnings}, your current balance is:${balance}, netting you an ROI of:{round(ROI, 2)}')
print("")
time.sleep(1.5)

while True: #Check to see if you won the big one
    if winning_ticket != ticket:
        print("Thank you for supporting the education system with your lottory purchases.")
        break
    if winning_ticket == ticket:
        print("Congrats, you won the big one! Where will you spend your millions?")
print("")
#This is the 100th line of code!!!!