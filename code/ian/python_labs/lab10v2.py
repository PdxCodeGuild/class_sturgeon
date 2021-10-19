import re
with open('practice.csv' , 'r') as file:
    lines = file.read().split('\n')

keys_list = re.split(',', lines[0])

#def add contact
def add_contact(c_list):
    new_contact = {
        keys_list[0] : input('Enter name: '),
        keys_list[1] : input('Enter favorite fruit: '),
        keys_list[2] : input('Enter favorite color: ')
    }
    c_list.append(new_contact)
    print(new_contact)

#def lookup
def lookup(contacts_list):
    search = input('Search name: ')
    for x, values in enumerate(contacts_list):
        if search in contacts_list[x][keys_list[0]]: 
                print(values)
                return values

#def update
def update(result):
    attribute = input('Attribute: ')
    if attribute in keys_list:
        print(result[attribute])
        result[attribute] = input('Enter update: ')
        print(result)

def erase(result):
    snap = input('Delete?: ')
    if snap == 'y':
        deleted.append(result)
        contacts.remove(result)
        print(f'Deleted Contacts - {deleted}')
        

deleted = []         
contacts = []
for i, line in enumerate(lines):
    person  = re.split(',', lines[i])
    for item in person:
        
        contact = {
            keys_list[0] : person[0],
            keys_list[1] : person[1],
            keys_list[2] : person[2]
        }
    if keys_list == person:
        continue
    else:
        contacts.append(contact)


while True:
    selection = input('''
    Enter a selection:
    ------------------
    Create - c
    Search - s
    Update - u
    Delete - d
    Exit   - e
    ''')
    if selection == 'c':
        add_contact(contacts)
    elif selection == 's':
        lookup(contacts)
    elif selection == 'u':
        update(lookup(contacts))
    elif selection == 'd':
        erase(lookup(contacts))
    elif selection == 'e':
        print('Goodbye')
        break
    else:
        print('Please enter a valid selection..')