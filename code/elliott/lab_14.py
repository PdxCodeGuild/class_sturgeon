import requests

response = (requests.get('https://icanhazdadjoke.com/',
                         headers={'accept': 'application/json'})).json()

user_response = input('Do you want a Dad joke? Y/N ').upper()

if user_response == 'Y':
    print(response['joke'])
elif user_response == "N":
    print('You are not leaving without a Dad joke bud:  ', response['joke'])
