#Opens CSV file
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

#convert the lines of text into a list of dictionaries, one dictionary for each user. 
#The text in the header represents the keys, the text in the other lines represent the values.

for i in lines:
    print(i)


def contact_maker(enter_list):
    contacts = []
    for each in enter_list:
        pass


    return contacts

