import requests


response = requests.get('https://favqs.com/api/qotd',
                        headers={'Content-Type': 'application/json'}).json()
quote = response['quote']['body']
author = response['quote']['author']

#print(f'{quote} By the author {author}')

#user_quote = input("Enter a phrase to search for a quote")
response1 = requests.get('https://favqs.com/api/quotes', params={'page': '<page>', 'filter': '<keyword>'},
                         headers={'Content-Type': 'application/json'}).json()
# https://favqs.com/api/quotes ? page=<page>&filter=<keyword>


print(response1)
