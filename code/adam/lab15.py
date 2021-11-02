# Lab 15: Quotes API
import requests
import time

# print("")
# welcome_message = "Welcome to the Library-Interface's Quotes Generator"
# for char in welcome_message:
#   print(char, end='', flush=True)
#   time.sleep(.01)
# time.sleep(.5)
# print("")

#Version 1
version1 = requests.get('https://favqs.com/api/qotd', params ={'format': 'json'}, headers={'User-Agent': 'My Library (https://github.com/Library-Interface)', 'accept': 'application/json'})
version1.encoding = 'utf-8' #set encoding to utf-8, not always necessary, but safeguard

author = version1.json()['quote']['author']
quote = version1.json()['quote']['body']

print(f'Version1: {quote} From: {author}')
print("")
#Version 2
def v2search():
    page = 1
    version2_keyword = input("Search quotes with a single word:-->")
    version2 = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={version2_keyword}', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Content-Type': 'application/json'})
    version2_results = version2.json()['quotes']
    for quote in version2_results:
        print(quote['body'] + " by " + quote['author'])
    while True:
        if input('Would you like to see the next page results? (y/n):-->').lower() != "n":
            page += 1
            version2 = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={version2_keyword}', headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"', 'Content-Type': 'application/json'})
            version2_results = version2.json()['quotes']
            for quote in version2_results:
                print(quote['body'] + " by " + quote['author'])
            if input('Would you like to see the next page results? (y/n):-->').lower() == "y":
                continue
            else:
                if input("Would you like to enter a new search term? (y/n):-->").lower() == 'y':
                    v2search()
                    break
                else:
                    print("Thank you for using the Library-Interface's Quotes Generator!")
                    break
        else:
            if input("would you like to enter a new search term? (y/n):-->").lower() == 'y':
                v2search()
                break
            else:
                print("Thank you for using the Library-Interface's Quotes Generator")
                break

v2search()
