import requests

response = requests.get('https://favqs.com/api/qotd', headers= {'Content-Type': 'application/json'})

data = response.json()

print(f"Quote - {data['quote']['body']}")
print(f"Author - {data['quote']['author']}")
print(f"Tags - {data['quote']['tags']}")