# contact list

# opening a csv spreadsheet and saving it seperated by lines
# first line is the headers
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')


# formatting the csv into a list of dictionaries
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

# formatting back into csv
def lst_of_dicts_to_csv (contacts):
    headers = [key for key in contacts[0]]
    contact_str = ','.join(headers) + '\n'
    counter = 0
    for contact in contacts:
        counter += 1
        if len(contacts) == counter:
            contact_str += f'{contact[headers[0]]},{contact[headers[1]]},{contact[headers[2]]}'
        else:
            contact_str += f'{contact[headers[0]]},{contact[headers[1]]},{contact[headers[2]]}\n'

    return contact_str



# C of CRUD REPL - creating a new record to add to the current file
def create_record (contacts):
    input_name = input('Enter the name you want to add: ')
    input_fav_fruit = input(f"Enter {input_name}'s favorite fruit: ")
    input_fav_color = input(f"Enter {input_name}'s favorite color: ")
    
    contact_dict = {
        'name' : input_name,
        'favorite fruit' : input_fav_fruit,
        'favorite color' : input_fav_color
    }
    contacts.append(contact_dict)
    return contacts



# find record
def retrieve_record (contacts):
    user_name = input('What name would you like to look up? ')
    for item in contacts:
        if item['name'] == user_name:
            return item
            
    else:
        return 'Name not found'



# update section in record
def update_record (contacts):
    record_to_update = retrieve_record(contacts)
    yes_no_update = input(f"Would you like to update this record?\n{record_to_update}\n'yes' or 'no': ")
    if yes_no_update == 'yes':
        attribute_to_update = input("What section would you like to update,\n'name', 'favorite fruit', or 'favorite color'? ")
        new_attribute = input(f"What would you like to change {attribute_to_update} to? ")
        for item in record_to_update:
            if item == attribute_to_update:
                record_to_update[item] = new_attribute
        return contacts
    else:
        return 'You made no new changes'



# delete record
def delete_record (contacts):
    record_to_delete = retrieve_record(contacts)
    yes_no_delete = input(f"Would you like to delete {record_to_delete}'s record? 'yes' or 'no' ")
    if yes_no_delete == 'yes':
        contacts.remove(record_to_delete)
        return contacts
    else:
        return 'You made no new changes'





# current file converted to a list of dictionaries
contacts = csv_to_lst_of_dicts(lines)
# print('original record', contacts)

while True:
    user_action = input("Would you like to 'create', 'retrieve', 'update', or 'delete' a record?\nOr type 'exit' to exit: ")
    if user_action == 'create':
        create_record(contacts)
    elif user_action == 'retrieve':
        retrieve_record(contacts)
    elif user_action == 'update':
        update_record(contacts)
    elif user_action == 'delete':
        delete_record(contacts)
    elif user_action == 'exit':
        break
    else:
        print()
    
updated_contacts = lst_of_dicts_to_csv(contacts)

with open('contacts.csv', 'w') as file:
    file.write(updated_contacts)