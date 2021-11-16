
import time
from tkinter import *
from bs4 import BeautifulSoup
import requests
import random
import pyautogui
import pyttsx3

clicked = False
weather = ""
# name = ""
big_city = ""
wind = ""
awaken_text = ""
user_text = ""
argument_text = ""
universe_text = ""



# window.geometry("1500x800+700+200") #the +700 +200 moves the box to the right and up a bit
# window.resizable(0,0)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
weather = ""
name = ""
big_city = ""
wind = ""
awaken_text = ""
user_text = ""
argument_text = ""
universe_text = ""

RESPONSES = ["That's why you ordered velcro gloves",
            "Goats have no upper front teeth",
            "Sans doubt, except, yeah, doubt",
            "The answer is within you... seek enlightenment",
            "You may rely on it, but don't actually",
            "Have you been like this since your vaccination?",
            "Not if this administration has anything to say about it",
            "Outlook good, unless you're involved",
            "When you know you know",
            "Signs point to yes, so it's a no for you",
            "Reply hazy, try again tomorrow",
            "Ask again later, much, much later",
            "Better not tell you now",
            "Cannot predict now, don't like you",
            "Concentrate and ask again, and again",
            "Don't count on it, you're not well liked",
            "The universe replies with: why are you here?",
            "Our sources describe an image of... no",
            "Did you smell that? You must have Covid",
            "Very doubtful, it's you after all"]

ARGUMENTS = ["This is unwise",
            "You really should've known better",
            "When you made this decision, your ancestors wept",
            "Why did you insist on being dumb?",
            "You realize this is all your fault",
            "When you woke up this morning, did you feel this would be a bad day?",
            "Those chips you were eating by the window as a kid, yeah, those were paint chips",
            "Messed up you did",
            "This is just turning out to be a bad day for you"
            ]

def hello_world(window):
    print(weather[:2:]) #check 2 digits of weather to use for checking here
    if int(weather[:2:]) > 32:
        speak("Who... am I?")
        helloWorld = Label(window, text="It's too dark to see anything, but the floor feels cold and hard a rock awkwardly presses into your back.", font = ('Arial', 25))
        helloWorld.grid(row = 0, column = 1)
        helloWorld2 = Label(window, text="You can taste copper faintly in your mouth and have trouble remembering any details before the here and now", font = ('Arial', 25))
        helloWorld2.grid(row = 1, column = 1)
        helloWorld3 = Label(window, text="Suddenly a large creature begins to crawl across your chest, it's about 9 inches long and has many legs", font = ('Arial', 25))
        helloWorld3.grid(row = 2, column = 1)
        intro(window)
    else:
        exit()
def intro(window):
    global awaken_text
    awaken_text = StringVar()
    awaken_text.set("\nWhat do you do?\n")

    #defining labels
    intro_message = Label(window, textvariable = awaken_text)
    intro_message.grid(row = 3, column = 1, padx = 5, pady = 5)

    #define buttons
    response = Button(window, text ='Smack that bug off and scream', command=lambda:advance(window))
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

# city_for_weather()

name = ""
def advance(window):
    speak("You smack the over-sized bug off of your chest, screaming frantically as it skimpers off")
    global name
    name=pyautogui.prompt("What is your name?", "Welcome to unknown location", "Your name goes here")
    awaken_text.set("You feel better")
    speak(f"You stand up, center yourself with a deep breath in, and a deep breath out. I am {name}, I am in control of my emotions. I am {name}, I am not about to panic, I can handle this. I am {name}, and this, can't, be real.")
    quote(window)

def quote(window):
    version1 = requests.get('https://favqs.com/api/qotd', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})
    version1.encoding = 'utf-8' #set encoding to utf-8, not always necessary, but safeguard

    author = version1.json()['quote']['author']
    quote = version1.json()['quote']['body']
    speak("you repeat the quote from" + author + "that your father once told you" + quote)
    advance_time(window)

def advance_time(window):
    time.sleep(1)
    speak("You feel your emotions falling into place")
    time.sleep(1.4)
    speak(f"you feel the gentle {wind} wind on your face in the {weather} °F air")
    speak("The rock beside your foot begins to glow. You pick it up")
    eightBall(window)
    # openNewWindow()


def eightBall(window):
    eightWindow = Toplevel(window)
    eightWindow.title("The 8-ball of the Universe")
    eightWindow.geometry("1200x200+500+50")
    Label(eightWindow, text= "Welcome to the 8 Ball of the Universe")
    box1 = Label(eightWindow, text="Simple Question (Like Magic 8 Ball): ")
    box2 = Label(eightWindow, text="The Universe responds: ")
    # box3 = Label(eightWindow, text="Argue with the Universe: ")
    box1.grid(row = 1, column = 1, padx = 5, pady = 5)
    box2.grid(row = 2, column = 1, padx = 5, pady = 5)
    # box3.grid(row = 2, column = 1, padx = 5, pady = 5)
    user_box = StringVar()
    global user_text
    user_text = Entry(eightWindow, textvariable=user_box, width = 60)
    universe_box = StringVar()
    global universe_text
    universe_text = Entry(eightWindow, textvariable=universe_box, width = 60)
    argument_box = StringVar()
    # global argument_text
    # argument_text = Entry(eightWindow, textvariable=argument_box, width=60)
    user_text.grid(row = 1, column = 2) #user asks
    universe_text.grid(row = 2, column = 2) #universe replies
    # argument_text.grid(row = 3, column = 2) #argue with 8 ball
    response = Button(eightWindow, text ='Click here for the answers you seek', command=response_question)
    exitbtn = Button(eightWindow, text ="Get me out of here!", command=exit)
    argue = Button(eightWindow, text ='What does that mean? You\'re and idiot!', command=lambda:arguments(window))
    response.grid(row = 5, column = 1, padx = 2, pady = 2)
    exitbtn.grid(row = 5, column = 2, padx = 1, pady = 1)
    argue.grid(row = 5, column = 3, padx = 1, pady = 1)

def response_question():
    x = random.choice(RESPONSES)
    universe_text.delete(0, END) # clear prev output
    universe_text.insert(0,str(x)) # insert response

clicked = False

def arguments(window):
    global clicked
    if not clicked:
        x = random.choice(ARGUMENTS)
        universe_text.delete(0, END) # clear prev output
        universe_text.insert(0,str(x)) # insert response
        openNewWindow(window)
        clicked = True
    else:
        challenging() # ALT + Shift and down arrow copies!
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()
        challenging()

def challenging(window):
    angryWindow = Toplevel(window)
    angryWindow.title("The Universe Is Very Angry!")
    angryWindow.geometry("400x50")
    Label(angryWindow, text = random.choice(ARGUMENTS)).pack()

def very_mad():
    pyautogui.alert(f"You really had to click it, didn't you?", f"Critical Mistake By {name}")
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    challenging()
    a=pyautogui.password('Computer locked. Password is the answer to 5*3-8+4', 'It\'s math, dummy')
    if a == 11:
        pyautogui.alert("That was spot on, but you're still a jerk")
    else:
        pyautogui.alert("That wasn't even close!", "You are not smart!")
        b=pyautogui.password('What color do you get when you mix green with red?')
        if b != 'nope':
            pyautogui.alert("Now you're just showing why you are never right", "It's almost like you care")
        else:
            print("You did it, you found the secret password")

def openNewWindow(window):
    
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
def start():
    city_for_weather()
    window = Tk()
    window.title('Welcome to the forest')
    window.configure(bg='black')
    window.attributes('-fullscreen', True)
    print("     ######################")
    print("     |                    |")
    print("     |  hello_world_game  |")
    print("     |                    |")
    print("     ######################")
    print("")
    time.sleep(1)
    pyautogui.alert('Wha... what happened to me? Where am I?')
    hello_world(window)
    
    window.mainloop() #This has to be on there to make the GUI work

if __name__=="__main__":   #If __name__ (name of this file) is being run as the main (not imported elsewhere)
    start()