#This mini-cap is two-fold. The first is an attempt to tackle the problem of a creepy landlord monitoring the router traffic and spying on tennants. To not be too depressing, there's also a game. 
import pyautogui
import background_app
import hello_world_game

pyautogui.alert(text='The background interference will flood your router with random information pulled from the Internet. The game is adventure-based', title='Informed Consent', button='Understood')
begin = pyautogui.prompt("Run background interference or play a game (background or game)?")
# begin = input("Would you like to run background interference or play a game (background or game)?:-->")
if begin == 'background':
    background_app.start()
if begin == 'game':
    hello_world_game.start()
if begin != 'background' and begin != 'game':
    print("you failed to enter game or backround")

print("Thank you for your time")