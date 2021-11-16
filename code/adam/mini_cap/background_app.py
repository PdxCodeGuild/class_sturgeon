#Interactive new idea
#install pywin32, pyttsx3, downloaded from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio PyAudio-0.2.11-cp39-cp39-win_amd64.whl for my version 3.9 python and went to download folder typed cmd to pull up prompt from there and pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl which is the name of the downloaded file
import time
from tkinter import *
from bs4 import BeautifulSoup
import requests
import random
import pyautogui

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
weather = ""
name = ""
big_city = ""
wind = ""
awaken_text = ""
user_text = ""
argument_text = ""
universe_text = ""

def get_weather(city):
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
    get_weather(city)

# city_for_weather()

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

def covid():
    response = requests.get('https://api.covidtracking.com/v1/states/current.json', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})
    response.encoding = 'utf-8' #set encoding to utf-8, not always necessary, but safeguard
    # print(response.json())
    covid_results = response.json()
    print(covid_results)
    for state in covid_results:
        print(state['state'] + " with " + str(state['positive']) + " total positive cases as of today")
    
weather_count = 0
minute = 10 #It takes 5-7 seconds (toc - tic) to perform the tasks

def get_city_news(city):
    print("")
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q=news+in+{city}', headers = headers)
    soup = BeautifulSoup(res.text,'html.parser')
    heads = soup.find_all( 'h3' )
    headline_utah = soup.find_all('div', {'class':'mCBkyc oz3cqf p5AXld nDgy9d'})
    headline_portland = soup.find_all('div', {'class': 'BNeawe vvjwJb AP7Wnd'})
    for info in headline_portland:
        print(info.getText())
    for info in heads:
        print(info.getText())
    for info in headline_utah:
        print(info.getText())
    print("")

def city_for_news():
    get_city_news(big_city)

def start():
    weather_count = 0
    while True:
        turn_on_time=pyautogui.prompt("How many minutes would you like to run the program?", "The anonymous surfuing tool", '1, 5, 10')
        # turn_on_time = input("How many minutes would you like to run the program? (ie 15, 30, 60):-->")
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
                time.sleep(.1)
                covid()
                time.sleep(random.randint(1,3))
                toc = time.perf_counter()
                print(f'Time to complete tasks this iteration: {toc - tic:0.2f} seconds') #The :0.4f is a format specifier that says I want 2 decimal points
            break
        else:
            print('You need to enter a number other than zero')

if __name__=="__main__":   #If __name__ (name of this file) is being run as the main (not imported elsewhere)
    start()