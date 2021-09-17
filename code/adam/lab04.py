#Lab04 Blackjack Advice
#Best Blackjack advice, never play in a casino
import time

print("")
welcome_message = "Welcome to the Library-Interface's Blackjack Advisor"
welcome_message2 = "You will be asked to provide 3 cards from (2,3,4,5,6,7,8,9,10,J,Q,K,A)"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
print("")
for char in welcome_message2:
  print(char, end='', flush=True)
  time.sleep(.01)
print("")

#Capitalizing the face cards to ensure user input doesn't break it
player_card1 = input("What is your first card?-->").capitalize()
player_card2 = input("What is your second card?-->").capitalize()
player_card3 = input("What is your third card?-->").capitalize()

def total(card1, card2, card3):
    total = 0
    #Player's First Card    
    if card1 == "J" or card1 == "Q" or card1 == "K":
        total += 10
    elif card1 == "A":
        if total >= 11:
            total += 1
        else:
            total += 11
    else:
        total += int(card1)
    #Player's Second Card
    if card2 == "J" or card2 == "Q" or card2 == "K":
        total += 10
    elif card2 == "A":
        if total >= 10: #reducing this to 10 to keep from busting
            total += 1
        else:
            total += 11
    else:
        total += int(card2)
    #Player's Third Card
    if card3 == "J" or card3 == "Q" or card3 == "K":
        total += 10
    elif card3 == "A":
        if total >= 10: #reducing this to 10 to keep from busting
            total += 1
        else:
            total += 11
    else:
        total += int(card3)
    #Determining soft hit below 17, stay 17-21, win at 21, and busted over 21   
    print("")
    print(f'You have a total of {total} and should follow advice: ')
    if total < 17:
        print("Hit")
    if total >= 17 and total < 21:
        print("Stay")
    if total == 21:
        print("Blackjack! (Don't hit, you won)")
    if total > 21: 
        print("Already Busted, choose smaller cards next time.")
    return total

approved_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
while True:
    if player_card1 not in approved_list:
        print(f"{player_card1} Is not an appropriate choice of card, enter a real card.")
        player_card1 = input("Enter a real card:-->").capitalize()
    else:
        break
    if player_card2 not in approved_list:
        print(f"{player_card2} Is not an appropriate choice of card, enter a real card.")
        player_card2 = input("Enter a real card:-->").capitalize()
    else:
        break
    if player_card3 not in approved_list:
        print(f"{player_card3} Is not an appropriate choice of card, enter a real card.")
        player_card3 = input("Enter a real card:-->").capitalize()
    else:
        break

total(player_card1, player_card2, player_card3)

print("")
print("Thank you for using the Library-Interface's Blackjack Advisor")