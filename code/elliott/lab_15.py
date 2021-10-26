import requests

while True:
    keyword = input("Enter a phrase to search for a quote: ")
    page = input('Enter page number or done: ')

    response = requests.get('https://favqs.com/api/quotes', params={'page': page, 'filter': keyword},
                            headers={'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}).json()

    quotes = response['quotes']

    amount_of_quotes = len(quotes)
    print(
        f'There are {amount_of_quotes} quotes associated with the keyword {keyword}. Page {page}')

    for quote in quotes:
        list_quotes = quote['body']
        print("--------------------------------------------------------------------" '\n', list_quotes)

    if page == 'done':
        break
