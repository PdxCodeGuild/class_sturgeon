#Lab 14: Dad Joke API
import time
import requests

print("")
welcome_message = "Welcome to the Library-Interface's Dad Joke Generator"
for char in welcome_message:
  print(char, end='', flush=True)
  time.sleep(.01)
time.sleep(.5)
print("")

#Version 1 of the dad joke generator
response = requests.get('https://icanhazdadjoke.com/', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})
response.encoding = 'utf-8' #set encoding to utf-8, not always necessary, but safeguard

print(response.json()['joke']) #Version 1

#Version 2 of the dad joke generator
print("")
search_term = input("Give a single word to search for in dad jokes:-->").lower()
search = requests.get(f'https://icanhazdadjoke.com/search?term={search_term}', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})

# print(search.json()['results'][0]['joke'])
joke_result = search.json()['results']
if len(joke_result) == 0:
    print("Your search returned no dad jokes, you're not punny")

joke_counter = 0
for jokes in joke_result:
    joke_counter += 1
    print(jokes['joke'])
    time.sleep(1.6)
    if joke_counter == 5:
        if input("Do you want to see the next 5? (y or n):-->") != 'y':
            break
        else:
            joke_counter = 0
print("")
print("Thank you for using the Library-Interface's Dad Joke Generator")