# contact list

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')


def csv_to_lst_of_dicts (lines):
    lst_of_lsts = []

    for line in lines:
        line = line.split(', ')

        for item in line:
            item = item.split(',')
            lst_of_lsts.append(item)

    headers = lst_of_lsts.pop(0)
    contacts = []

    for list in lst_of_lsts:
        contacts.append({
            headers[0] : list[0],
            headers[1] : list[1],
            headers[2] : list[2]
        })
    return contacts


contacts = csv_to_lst_of_dicts(lines)


def create_record (contacts):
    new_contact = []

    while True:
        user_answer = input("Would you like to enter a new contact, 'yes' or 'no': ")
        if user_answer == 'yes':
            input_name = input('Enter the name you want to add: ')
            new_contact.append(input_name)
            input_fav_fruit = input(f"Enter {input_name}'s favorite fruit: ")
            new_contact.append(input_fav_fruit)
            input_fav_color = input(f"Enter {input_name}'s favorite color: ")
            new_contact.append(input_fav_color)
        if user_answer == 'no':
            break

    contact_dict = {
        'name' : new_contact[0],
        'favorite fruit' : new_contact[1],
        'favorite color' : new_contact[2]
    }
    contacts.append(contact_dict)
    #print(new_contact)
    #return contact_dict

print(create_record(contacts))
#new_contact = create_record()
#contacts.append(new_contact)
print(contacts)

def retrieve (contacts):
    #ask user for name
    user_name = input('What name would you like to look up? ')
    for item in contacts:
        if item['name'] == user_name:
            return item
        # else:
        #     print('Name not found')

print(retrieve(contacts))

