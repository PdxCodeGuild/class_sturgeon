import requests

def random_quote():
    theresponse = requests.get('https://favqs.com/api/qotd' , headers={'accept': 'application/json'})

    x = theresponse.json()
    quote = str(x['quote']['body'])
    author = str(x['quote']['author'])

    return f'\n"{quote}"\n\n by {author}'

def search_quote_by_keyword(keyword, page):

    keyword = ' ' + keyword + ' '
    theresponse = requests.get(f'https://favqs.com/api/quotes?page={page}&filter={keyword}' , headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    x = theresponse.json()
    multiple_dic = x['quotes']
    
    if len(multiple_dic) <= 1:
        print(f"\n>>>>>>>>>> Sorry but there are no quotes found on page {x['page']} with the word '{keyword}'")

    else:
        print(f"\n>>>>>>>>>> There are {len(multiple_dic)} quotes associated with the word '{keyword}' on page {x['page']}: ")

        for single_dic in multiple_dic:
            quote = str(single_dic['body'])
            author = str(single_dic['author'])
            print(f'\n"{quote}"\nby {author}')
    
    return True

while True:

    keyword = input(f'\n Choose your option:\n\n enter "random" -- if you like a random quote\n enter "exit" -- of exit the program\n\n or enter the word you wish to search...\n >>>> ').lower()

    if keyword == 'exit':
        break
    
    elif keyword == 'random':
        print(random_quote())
        
    else:
        page = 0
        choice = 'notdone'
        
        while True:
            page += 1
            search_quote_by_keyword(keyword, page)
            choice = input(f'\n >>>>>>>>>>>>Enter "next page" or "done": ')

            if choice == "done" or page > 24 :
                break

print(f'\n>>>>>>>> OK! Bye bye')



