#Opens CSV file
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

nested_list = [each.split(",") for each in lines]

keys = nested_list[0]
data = []

for i, values in list(enumerate(nested_list))[1::]:
    data.append(dict(zip(keys,values)))


"""_____________________Version 2_____________""" 
def create_contact(key, data):   
    new_contact = {}
    for key in keys:
        new_contact[key] = input(f"What is your new contact's {key}: ")
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
"""

while True:
    client_input = input("What would you like to do to a record? (C)reate? (R)ead? (U)pdate? (D)elete? ")
    if client_input == "C":
       create_contact(data, keys)
    elif client_input == "R":
        read_contact(data, keys)
    elif client_input == "U":
        update_contact(data, keys)
    elif client_input == "D":
        delete_contact(data, keys)
    else: 
        print("Wrong command, bud")
    break
