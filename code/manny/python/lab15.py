import requests
import time

web_response = requests.get("https://favqs.com/api/qotd", headers={'accept': 'application/json'})
web_quotes = web_response.json()

quote = str(web_quotes['quote']['body'])
author = str(web_quotes['quote']['author'])

print("The venerable " + author + " once said, \"" + quote + "\"" )


"""_____________________________Version 2 _____________________________"""

user_keyword = input("Enter a keywork to search for related quotes: ")
page = 1

while True:
    print(page, user_keyword)
    keyword_search = requests.get("https://favqs.com/api/quotes?", params = {"page" : page, "filter" : user_keyword}, headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, )
    keyword_search = keyword_search.json()
    things = keyword_search['quotes']

    for each in things:     
        print(each['body'] + " - " + each['author'] + "\n")
        time.sleep(2.3)

    duck = input("Would you like to see the next page? ")
    
    if duck.lower() not in ["y", "yes", "another"]:
        break
    else:
        page += 1 