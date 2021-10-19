import requests
import time
import re
response = requests.get('https://icanhazdadjoke.com', headers= {'accept': 'application/json'})

data = response.json()




dad_joke = data['joke']
split_joke = re.split('[?.,]', dad_joke)
for i in split_joke:
    print('\n' + i) ; time.sleep(2)



