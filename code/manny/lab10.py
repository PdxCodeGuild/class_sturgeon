import re
#Opens CSV file
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

#Final Contact list
contact_list_complete = []    

#Splits list, uses for loors to create dict's and appends to final list
def contact_maker(contacts):
    nested_list = [each.split(",") for each in contacts]
    person_marker = 1
    num_people = len(nested_list[0]) - 1 

    for babuska in range(num_people):
        key_marker = 0
        contact_dict = {}
        
        for matryoshka in nested_list:
            key = nested_list[key_marker][0]
            person = nested_list[key_marker][person_marker]
            key_marker += 1
            contact_dict.update({key:person})
        
        person_marker += 1
        contact_list_complete.append(contact_dict)
    print(contact_list_complete)

contact_maker(lines)

"""__________________Verson 2____________________"""

def create_contact(data, keys):
    new_contact = {}
    for key in keys:
        new_contact [key] = input(f"What is your new contact's {key}")
    data.append(new_contact) 

def read_contact(data, keys):
    #first we need a list of keys
    key_string = "\n" + "\n".join(keys) + "\n"
    key = input(f"What would you like your search by, search from {key_string}")

    contact_input = input("What is your search category")

    data_results = []
    for contact in data:
        if contact[key_input] == contact_input:
            data_results.append(contact)
    print(data_resuts)

    ORRR

    data_results = list(filer(lamda contact: contact[key_input] == contact_input,data))
    #this defines a type of function and I have absolutely no idea what to do. 

def update_contact(data, keys):
    pass 

    data_results = read_contact(data, keys)

    index_to_update = int(input(f"which contacd do you want to edit? {len{data_results)}"))
    key_to_update = input(f"{keys}")


def delete_contact(data, keys):
    pass

while True:
    client_input = input("What would you like to do to a record? Create? Read? Update? Delete?")
    if client_input == "create":
        pass #write the funciton about the input
    elif client_input == "read":
        pass
    elif client_input == "update":
        pass
    elif client_input == "delete":
        pass
    else: 
        print("Wrong command, bud")
    break

"""___________________________Version 3________________________________"""

data_csv_output = []

data_csv_output.append(keys)

for contact in data:
    data_csv_output.append(list(contact.values))

print(data_csv_output) #this should print out lines

data_csv_output = [",".join(line) for line in data_csv_output]

data_csv_output = "\n".join(data_csv_output)

print(data_csv_output)

with open("contacts_copy.csv", "w") as f:
    f.write(data_csv_output)

