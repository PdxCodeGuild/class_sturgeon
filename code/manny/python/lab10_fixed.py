#Opens CSV file
with open('contacts_copy.csv', 'r') as file:
    lines = file.read().split('\n')

nested_list = [each.split(",") for each in lines]

keys = nested_list[0]
data = []

for i, values in list(enumerate(nested_list))[1::]:
    data.append(dict(zip(keys,values)))

"""________________________________Version 2________________________________""" 

def create_contact(key, data):   
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f"What is your new contact's {key}: ")
    data.append(new_contact) 

def read_contact(data, keys):
    key_string = "\n" + "\n".join(keys) + "\n"
    key_search = input(f"What would you like your search by, search from {key_string}")
    search_term = input("What term would you like to look by? ")
    search_results = []
    
    for contact in data:
        if contact[key_search] == search_term:
            search_results.append(contact)
    print(search_results)

def update_contact(data, keys):
    data_results = read_contact(data, keys)
    data_results = len(data_results) -1 
    index_to_update = int(input(f"Which contact do you want to edit? {data_results} ")) 
    key_to_update = input(f"Which key would you like to update? {keys} ")
    value_to_update = input(f"What do you want to change {key_to_update} to? ")
    data_results[index_to_update][key_to_update] = value_to_update

def delete_contact(data, keys):
    data_results = read_contact(data, keys)
    data_results = len(data_results) - 1
    index_to_delete = int(input(f"Which contact do you want to delete? {data_results}"))
    data.remove(data_results[index_to_delete])

while True:
    client_input = input("What would you like to do to a record? (C)reate? (R)ead? (U)pdate? (D)elete? ")
    client_input = client_input.lower()
    if client_input == "c":
       create_contact(data,keys)
    elif client_input == "r":
        read_contact(data, keys)
    elif client_input == "u":
        update_contact(data, keys)
    elif client_input == "d":
        delete_contact(data, keys)
    else: 
        print("Wrong command")
        break

"""________________________________Version 3________________________________""" 