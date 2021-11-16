#Interactive new idea
#install pywin32, pyttsx3, downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio PyAudio-0.2.11-cp39-cp39-win_amd64.whl for my version 3.9 python and went to download folder typed cmd to pull up prompt from there and pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl which is the name of the downloaded file
import time
from tkinter import *
from bs4 import BeautifulSoup
import requests
import random
import pyautogui
import pyttsx3

window = Tk()
window.title('Welcome to the forest')
window.configure(bg='black')
window.attributes('-fullscreen', True)
frame = Frame(window)
# window.geometry("1500x800+700+200") #the +700 +200 moves the box to the right and up a bit
# window.resizable(0,0)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
weather = ""
name = ""
big_city = ""
wind = ""
awaken_text = ""

def hello_world():
    speak("Who... am I?")
    helloWorld = Label(window, text="It's too dark to see anything, but the floor feels cold and hard a rock awkwardly presses into your back.")
    helloWorld.grid(row = 0, column = 1)
    helloWorld2 = Label(window, text="You can taste copper faintly in your mouth and have trouble remembering any details before the here and now")
    helloWorld2.grid(row = 1, column = 1)
    helloWorld3 = Label(window, text="Suddenly a large creature begins to crawl across your chest, it's about 9 inches long and has many legs")
    helloWorld3.grid(row = 2, column = 1)
    intro()

def intro():
    global awaken_text
    awaken_text = StringVar()
    awaken_text.set("\nWhat do you do?\n")

    #defining labels
    intro_message = Label(window, textvariable = awaken_text)
    intro_message.grid(row = 3, column = 1, padx = 5, pady = 5)

    #define buttons
    response = Button(window, text ='Smack that bug off and scream', command=advance)
    exitbtn = Button(window, text ="Forget it <roll over> wake me when it's over!", command=exit)

    #place buttons
    response.grid(row = 4, column = 0, padx = 6, pady = 1)
    exitbtn.grid(row = 4, column = 2, padx = 6, pady = 1)


def weather(city):
    global wind
    global weather
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers = headers)
    print("Running next random weather search......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    # time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    # precipitation = soup.select_one('#wob_pp').text
    # humidity = soup.select_one('#wob_hm').text
    wind = soup.select_one('#wob_ws').text
    # current_time = soup.select_one('#wob_dts').text
    print(location)
    # print(time)
    print(info)
    
    print(wind)
    # print(humidity)
    # print(precipitation)
    print(weather+"°F") 
    # print(current_time)

def city_for_weather():
    city_name = ['orem','provo','forks','portland','seattle','spokane', 'las vegas', 'salt lake city', 'ogden', 'logan', 'wendover', 'reno', 'phoenix','denver', 'chicago', 'miami', 'new york city', 'des moines']
    city = random.choice(city_name)
    city=city+" weather"
    global big_city
    big_city = city
    weather(city)

city_for_weather()

def advance():
    global name
    speak("You smack the over-sized bug off of your chest, screaming frantically as it skimpers off")
    name=pyautogui.prompt("What is your name?", "Welcome to unknown location", "Your name goes here")
    awaken_text.set("You feel a lot better now")
    speak(f"You stand up, center yourself with a deep breath in, and a deep breath out. I am {name}, I am in control of my emotions. I am {name}, I am not about to panic, I can handle this. I am {name}, and this, can't, be real.")
    advance_time()

def advance_time():
    time.sleep(1)
    speak("You feel your emotions falling into place")
    openNewWindow()

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("You notice a slight breeze coming from somewhere to the right of you")
 
    # sets the geometry of toplevel
    newWindow.geometry("1200x100+500+100")
    newWindow.configure(bg='black')
    time.sleep(1)
    speak("You hear a large creature somewhere behind you stirring out of a slumber")
    # A Label widget to show in toplevel
    # new_window_question = Label(newWindow, text ="What do you do?")
    # new_window_question.grid(row = 0, column = 1)
 
     # Define button
    runAway = Button(newWindow, text = 'I am not sticking around here <get up and run>', command=run).pack()
    giveUp = Button(newWindow, text="It's all over man <curls up in ball and cries>", command=newWindow.destroy).pack()

    # Place button
    runAway.grid(row = 1, column = 0, padx = 1, pady = 1)
    giveUp.grid(row = 1, column = 2, padx = 1, pady = 1)

def run():
    pyautogui.alert(f"Come on {name}, get it together! What's that white light?", "You feel a sharp pain in your neck...")
    challenging()
    exit()

def challenging():
    # angryWindow = Toplevel(window)
    # angryWindow.title("Hakunamatata")
    # angryWindow.geometry("400x50+500+100")
    # angry_label = Label(angryWindow, text = "nope")
    # angry_label.grid(row = 8, column = 1)
    speak("What was that feeling in my neck? No Matter, you see a light and head towards it...")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# speak(f"You awaken in an open field with the sound of birds chirping in the surrounding forest {wind} wind blowing over your body under the {weather} degree sun")
# time.sleep(1)
# speak("You hear the sound of birds chirping in the nearby trees and feel an insect crawling across your chest")
# time.sleep(1)

print("     ######################")
print("     |                    |")
print("     |   Rematerialized   |")
print("     |                    |")
print("     ######################")
print("")
time.sleep(1)

pyautogui.alert('Wha... what happened to me? Where am I?')
hello_world()
window.mainloop() #This has to be on there to make the GUI work