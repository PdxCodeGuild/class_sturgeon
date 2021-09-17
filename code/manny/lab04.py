"""Lab 4"""
#Key value pairs assigns value to card

card_points = {
    "A" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10, 
    "Q" : 10, 
    "K" : 10
}

player_hand = []
hand_value = 0

card_1 = input("What is your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")

#checks if inputs are valid
 
if card_1 and card_2 and card_3 in card_points: 
    print("Thank you. Dispansing sage advice...")
else: 
    print("Please use appropriate inputs next time.")
    quit()
        
#Appends value to empty list
if card_1 in card_points: 
    player_hand.append(card_points[card_1])
if card_2 in card_points:
    player_hand.append(card_points[card_2])
if card_3 in card_points:
    player_hand.append(card_points[card_3])

#Total value of cards
for num in player_hand: 
    hand_value += num

#Dispenses advice
if hand_value < 17: 
    print("Hit!")
elif 17 <= hand_value < 21:
    print("Stay!")
elif hand_value == 21: 
    print("BLACKJACK!")
else: 
    print("Already busted")








