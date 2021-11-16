import requests

theresponse = requests.get('https://icanhazdadjoke.com/' , headers={'accept': 'application/json'})

x = theresponse.json()
y = str(x['joke'])

print(f'\n {y} \n')
