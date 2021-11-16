"""Lab 5"""
import random

#Generate a list of 6 random numbers representing the winning tickets
winning_ticket = [random.randint(1,100) for digits in range(6)]
winning_ticket.sort()
print(f"These are the winning numbers: {winning_ticket} \nBest of luck! \nRemember the government gets 50% of everything you win!")
#Start your balance at 0 and ask the user how many times they want to play.
win_purse = 0
how_many = int(input("How many tickets do you want to buy? ")) #For now, lets assume the customer only inputs digits

#Function takes how many tickets they want to play, and compares it to the winning ticket from earlier. Annoucing each lottery number and if they won, then prints out the total values.
def vegas_alternative(how_many, winning_ticket, win_purse=0):
    while how_many > 0:
        ticket_purchased = [random.randint(1,100) for hope in range(6)]
        win_purse -= 2
        how_many -= 1
        ticket_purchased.sort()
        print(ticket_purchased)
        win_pick = 0
        for pick in ticket_purchased:
            if pick in winning_ticket:
                win_pick += 1 
        if win_pick == 1:
            win_purse += 4
            print("Nice, you doubled your money.")
        elif win_pick == 2:    
            win_purse += 7 
            print("Cool, you can get a sandwich.")
        elif win_pick == 3:    
            win_purse += 100
            print("Awesome, two tanks of gas!")
        elif win_pick == 4:    
            win_purse += 50000
            print("Wow! Goodbye student loans!! Hawaii, here we come!")
        elif win_pick == 5:  
            win_purse += 1000000
            print("Invest in real estate! You suddenly have strong opinions on taxes!")
        elif win_pick == 6:  
            win_purse += 25000000
            print("You just won half what NBA superstars players make in a year. Congratulations! Go Lakers!")
    print(f"After {how_many} lotter tickets, you have {win_purse} dollars!")

vegas_alternative(how_many, winning_ticket)