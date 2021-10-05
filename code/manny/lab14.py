import requests

#gets requests from dad jokes . com, 
response = requests.get('https://icanhazdadjoke.com', headers={'accept': 'application/json'})
#gets data as json
data = response.json()

#prints responses to client
print("\nWanna hear a bad joke?\n")
print(f"{data['joke']}\n")
