# dad joke api

import requests
import time
import re


while True:
    search_term = input('What subject would you like dad jokes about? "e" to exit\n')
    response = requests.get('https://icanhazdadjoke.com/search?term=' + search_term, headers={'accept': 'application/json'})
    jokes = response.json()['results']
    if search_term == 'e':
        break
    else:
        for joke in jokes:
            print(joke['joke']+'\n')
            another = input('Do you want to hear another one? "y" or "n"\n')
            if another != 'y':
                break
            
    # joke_words = joke.split(' ')
    # joke = re.split('[?,.]', response.json()['joke'])
    #print(jokes)
   



#print(joke)
# print(joke[0] + '?')
# time.sleep(3)
# print(joke[1][1::])

