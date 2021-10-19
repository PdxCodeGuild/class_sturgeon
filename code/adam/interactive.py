#Interactive new idea
import time
from tkinter import *
from bs4 import BeautifulSoup
import requests
import random
import pyautogui


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
big_city = ""
wind = ""
weather = ""
name = ""

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

#The window
window = Tk()
window.title('Welcome to the fun house')
window.geometry('1200x100')
window.resizable(0,0)

def run():
    pyautogui.alert(f"Come on {name}, get it together! What's that white light?", "You feel a sharp pain in your neck...")
    challenging()
    exit()

def challenging():
    angryWindow = Toplevel(window)
    angryWindow.title("The Universe Is Very Angry!")
    angryWindow.geometry("400x50")
    Label(angryWindow, text = "nope").pack()

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("The birds have stilled, warning you that there is a predator nearby")
 
    # sets the geometry of toplevel
    newWindow.geometry("1200x100")
 
    # A Label widget to show in toplevel
    Label(newWindow, text ="There is a rustling in the trees on the near side of the open field...\nSomething large approaches").pack()
 
     # Define button
    challenge = Button(newWindow, text = 'I am not sticking around here <get up and run>', command=run).pack()
    sorry = Button(newWindow, text="It's all over man <curls up in ball and cries>", command=newWindow.destroy).pack()
   
    # Place button
    challenge.grid(row = 5, column = 1, padx = 1, pady = 1)
    sorry.grid(row = 5, column = 2, padx = 1, pady = 1)

def advance_time():
    time.sleep(1)
    openNewWindow()

def advance():
    global name
    name=pyautogui.prompt("What is your name?", "Welcome to the forest", "Your name goes here")
    awaken_text.set("You stand up, take a few breaths and try to collect your calm")
    advance_time()

awaken_text = StringVar()
awaken_text.set(f"You awaken in an open field with the sound of birds chirping in the surrounding forest.\n The " + wind + " wind blowing over your body under the " + weather + "°f sun")

#defining labels
intro_message = Label(window, textvariable = awaken_text)
intro_message.grid(row = 1, column = 2, padx = 5, pady = 5)

#define buttons
response = Button(window, text ='Commit to exploring the area to discover what is going on', command=advance)
exitbtn = Button(window, text ="Forget it <roll over> wake me when it's over!", command=exit)

#place buttons
response.grid(row = 2, column = 1, padx = 6, pady = 1)
exitbtn.grid(row = 2, column = 3, padx = 6, pady = 1)

window.mainloop() #This has to be on there to make the GUI work