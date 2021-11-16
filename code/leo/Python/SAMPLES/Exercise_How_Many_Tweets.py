'''
You've got a very important message to get out to all your followers on Twitter. Unfortunately, Twitter only allows 280 characters per Tweet. Your message is over 1,000 characters long and you're wondering how many Tweets it will take to get your whole message out.

3.1
Calculate the number of Tweets required, rounding up to the nearest integer.

3.2
Ask the user for the number of characters in their message

if the length of the message is less than the max_length allowed for a Tweet, output a message telling the user they only need one Tweet

Otherwise, calculate the number of Tweets required, rounding up to the nearest integer and output a message telling the user the number of Tweets they will need.

3.3
Display different messages to the user depending on how many Tweets their message requires.'''

max_lenght = 280

number_of_characters = int(input('Enter the number of characters: '))

if number_of_characters <= max_lenght :
    
    print(f'Your tweet has "{number_of_characters}", you will be able to send your message in only one tweet')

elif number_of_characters > max_lenght :
    
    tweets = int(number_of_characters / max_lenght)
    
    print(f'''
    Your tweet has "{number_of_characters}", witch pass the limit of "{max_lenght}".
    If you want to send out the the entire message, it will take you at lease "{tweets}" tweets to sent out your message.
    ''')


