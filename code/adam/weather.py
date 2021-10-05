#I saw an article about a landlord monitoring the router for traffic to spy on a female tennant. I'm not sure how to counter that professionally, but I figure a program that randomly does things interacting with the internet might be a good start. So here we are.
#Need to pip install BeatifulSoup
#ending with smart-alick 8 ball for fun

from bs4 import BeautifulSoup
import requests
import random
import time
from tkinter import *

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#This code would request a page simulating to be Googlebot. otherwise, Google will block requests eventually

big_city = ""

def weather(city):
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers = headers)
    print("Running next random weather search......\n")
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
    precipitation = soup.select_one('#wob_pp').text
    humidity = soup.select_one('#wob_hm').text
    wind = soup.select_one('#wob_ws').text
    current_time = soup.select_one('#wob_dts').text
    print(location)
    print(time)
    print(info)
    print(wind)
    print(humidity)
    print(precipitation)
    print(weather+"°F") 
    print(current_time)

def city_for_weather():
    city_name = ['orem','provo','clearfield','portland','seattle','spokane', 'las vegas', 'salt lake city', 'ogden', 'logan', 'wendover', 'reno', 'phoenix','denver', 'chicago', 'miami', 'new york city', 'des moines']
    city = random.choice(city_name)
    city=city+" weather"
    global big_city
    big_city = city
    weather(city)

def v3search():
    page = 1
    version2_keyword = random.choice(['car', 'van', 'apple', 'boy', 'girl', 'whistle', 'hair', 'pizza', 'dark', 'doll', 'swim', 'ocean'])
    version2 = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={version2_keyword}', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Content-Type': 'application/json'})
    version2_results = version2.json()['quotes']
    for quote in version2_results:
        print(quote['body'] + " by " + quote['author'])

def dad_joke():
    response = requests.get('https://icanhazdadjoke.com/', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})
    response.encoding = 'utf-8' #set encoding to utf-8, not always necessary, but safeguard
    print(response.json()['joke']) #Version 1

weather_count = 0
minute = 10 #It takes 5-7 seconds (toc - tic) to perform the tasks

def get_city_news(city):
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q=news+in+{city}', headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    heading = soup.find_all( 'h3' )
    for info in heading:
        print(info.getText())

def city_for_news():
    get_city_news(big_city)

while True:
    turn_on_time = input("How many minutes would you like to run the program? (ie 15, 30, 60):-->")
    if turn_on_time.isdigit() and turn_on_time != '0':
        turn_on_time = abs(int(turn_on_time))
        turn_on_time = turn_on_time * minute
        while weather_count < turn_on_time:
            weather_count += 1
            tic = time.perf_counter()
            dad_joke()
            time.sleep(.3)
            city_for_weather()
            time.sleep(.12)
            city_for_news()
            time.sleep(.1)
            v3search()
            time.sleep(random.randint(1,3))
            toc = time.perf_counter()
            print(f'Time to complete tasks this iteration: {toc - tic:0.2f} seconds') #The :0.4f is a format specifier that says I want 2 decimal points
        break
    else:
        print('You need to enter a number other than zero')

#The window
window = Tk()
window.title('Something like a Magic 8 Ball')
window.geometry('600x100')
window.resizable(0,0)
 
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

def response():
    msg = "Yo, only words here!"
    check_text = user_text.get()
    number_and_zero_entry_check = check_text.isdigit()
    length = len(user_text.get())
    #print length
    if number_and_zero_entry_check == True or length == 0:
        user_text.insert(0,(msg))

    else:	
        x = random.choice(RESPONSES)
        universe_text.delete(0, END) # clear prev output
        universe_text.insert(0,str(x)) # insert response
 
#define labels - cannot share same name as function
box1 = Label(window, text="Simple Question (Like Magic 8 Ball): ")
box2 = Label(window, text="The Universe responds: ")       

#place labels
box1.grid(row = 1, column = 1, padx = 5, pady = 5)
box2.grid(row = 2, column = 1, padx = 5, pady = 5)
 
#define user entry box 
user_box = StringVar()
user_text = Entry(window, textvariable=user_box, width = 60)
 
#define universe reply box 
universe_box = StringVar()
universe_text = Entry(window, textvariable=universe_box, width = 60)

#display boxes
user_text.grid(row = 1, column = 2,) #user asks
universe_text.grid(row = 2, column = 2,) #universe replies

#define buttons
response = Button(window, text ='Click here to seek your answer', command=response)
exitbtn = Button(window, text ='Go Away!', command=exit)

#place buttons
response.grid(row = 5, column = 1, padx = 2, pady = 2)
exitbtn.grid(row = 5, column = 2, padx = 1, pady = 1)

window.mainloop() #This has to be on there to make the GUI work