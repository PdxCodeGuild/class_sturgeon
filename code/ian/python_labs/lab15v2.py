import requests

command = 's'
search = []
while True:
    
    
    page = 1
    if command == 'done':
        print('Goodbye.')
        break
    elif command == 'next page':
        term = search[0]
        page += 1
    elif command == 's':
        term = input('Enter a search term: ')
        search.append(term)
    
    
    response = requests.get('https://favqs.com/api/quotes', 
    headers= {'Content-Type': 'application/json', 'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, 
    params= {'filter' : term, 'page' : page})

    data = response.json()

    for i in data['quotes']:
        print(f"Quote - {i['body']}")
        print(f"Author - {i['author']} \n")
    
    command = input("Enter 'next page' or 'done': ")


