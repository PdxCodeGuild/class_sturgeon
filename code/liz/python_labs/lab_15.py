# quotes api

import requests

while True:
    page = 1
    user_keyword = input("enter a keyword to search for quotes: 'e' to exit\n")
    if user_keyword == 'e':
        print('Goodbye')
        break

    while True:
        response = requests.get("https://favqs.com/api/quotes?", params={'page': page, 'filter': user_keyword}, headers={'accept': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    
        list_of_quotes = response.json()['quotes']
        for quote in list_of_quotes:
        
            body = quote['body']
            author = quote['author']
            print(f'"{body}"\n- {author}\n\n')
        
        command = input("enter 'next page' or 'done': ")
        if command == 'done':
            break
        elif command == 'next page':
            page += 1
            continue
        else:
            print('Command not recognized')
