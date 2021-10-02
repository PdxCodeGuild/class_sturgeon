# dad joke api

import requests
import time
import re


while True:
    search_term = input('What subject would you like dad jokes about? ')
    response = requests.get('https://icanhazdadjoke.com/search?term=' + search_term, headers={'accept': 'application/json'})
    # response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
    jokes = response.json()['results']
    for joke in jokes:
        print(joke['joke']+'\n')
    # joke_words = joke.split(' ')
    # joke = re.split('[?,.]', response.json()['joke'])
    #print(jokes)
   



#print(joke)
# print(joke[0] + '?')
# time.sleep(3)
# print(joke[1][1::])

