import requests
import time
import re
#response = requests.get('https://icanhazdadjoke.com/search', headers= {'accept': 'application/json'}, params= {'term' : 'skeleton'})

#data = response.json()
#print(data)

while True:

    print('Welcome to the joke generator!')
    command = input('(s)earch / (e)xit\n')
    if command == 'e':
        print('Goodbye.\n')
        break
    elif command == 's':
        term = input('Enter a search term: ')
        
        response = requests.get('https://icanhazdadjoke.com/search', headers= {'accept': 'application/json'}, params= {'term' : term})
        
        data = response.json()



    while True:
        
        for i, line in enumerate(data['results']):
            

            dad_joke = line['joke']
            split_joke = re.split('[?.,]', dad_joke)
            for i in split_joke:
                print('\n' + i) ; time.sleep(2)
            
            another_joke = input('Wanna hear another? y/n: ')
            if another_joke == 'n':
                print("okay, thats enough of those.\n")
                break
            
            elif another_joke not in ['y', 'n']:
                another_joke = input('Invalid selection..')
        if another_joke == 'n':
            break

command = input('To search again, enter (s) to exit enter (e)')


