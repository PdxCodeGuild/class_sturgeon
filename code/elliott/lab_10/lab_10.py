# ---------------------------------------------csv file-------------------------------------------------#
contacts = []

with open('code/elliott/lab_10/back_contacts.csv', 'r') as file:
    data = file.read().split('\n')
    #print("the csv data", data)
    # split()
    # join()
    csv_header = True
    for line in data:
        if csv_header:
            dict_keys = " ".join(line.split()).split(',')
            csv_header = False
            #print("these are the dict keys", dict_keys)
        else:
            values = " ".join(line.split()).split(',')
            contacts.append({dict_keys[n]: values[n]
                            for n in range(0, len(dict_keys))})
            #print("these are the dict values", values)

# ---------------------------------------------Create record--------------------------------------------------#
user_values = input("Enter a name,favorite fruit and favorite color. ")
values = user_values.split(',')
new_dict = {}

for i in range(len(values)):
    new_dict[dict_keys[i]] = values[i]
contacts.append(new_dict)

print("Added to contacts: ", contacts)
# elliott,apple,red


# ---------------------------------------------Retrieve record--------------------------------------------------#
# getting mutiple elliotts(contact i created)
name = input("Enter the contact name: ")
found_values = []

for dictionary in contacts:
    if (dictionary['name'] == name):
        found_values.append(dictionary)
        break

print("Requested contact: ", found_values)


# ---------------------------------------------update record--------------------------------------------------#

name1 = input("Enter the contact name: ")
attribute = input(
    "What item would you like to change? Pick: (name, favorite color, favorite fruit) ")
new_value = input("Enter new information: ")

dictionary = []
for dictionary in contacts:
    if (dictionary['name'] == name1):
        for key in dictionary:
            if key == attribute:
                dictionary['name'] = new_value

                print(contacts)

# ---------------------------------------------Delete record--------------------------------------------------#
name = input("Enter the contact name to be deleted: ")


for i in range(len(contacts)):
    if contacts[i]['name'] == name:
        del contacts[i]
        break

print("Del Contact:", contacts)


# ---------------------------------------------csv write--------------------------------------------------#
print('Contacts: \n', contacts)
'\n'
'\n'

names = [i["name"] for i in contacts]
favorite_fruit = [i['favorite fruit'] for i in contacts]
favorite_color = [i['favorite color'] for i in contacts]
header = 'name' 'favorite fruit' 'favorite color'


print(favorite_fruit, favorite_color)
'''
def listToString(a):
    str1 = " "
    return (str1.join(a))


h = listToString(header)
n = listToString(names)
fc = listToString(favorite_color)
ff = listToString(favorite_fruit)

final_write = header, '\n', n, '\n', fc, '\n', ff

with open('code/elliott/lab_10/back_contacts.csv', 'w') as file2:
    file2.write(final_write)
# elliott,apple,red




for f in contacts:
        fruits = f['favorite fruit']
        for c in contacts:
            color = c['favorite color']
new_data = list(contacts.items())


for n in len(contacts):
    names = n['name']
    for f in contacts:
        fruits = f['favorite fruit']
        for c in contacts:
            color = c['favorite color']

print(names, fruits, color)


# with open('code/elliott/lab_10/back_contacts.csv', 'w') as file2:
# file2.write(contacts)


# elliott,apple,red



new_dict.items()

new_data = list(new_dict.items())
print("new data", new_data)

k = list(new_dict.keys())
print("keys: ", k)

v = list(new_dict.values())
print("values: ", v)

new_file = ' '.join(map(str, v))
print("new file: ", new_file)


Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

Update a record: ask the user for the contact's name, then for which attribute of the user 
they'd like to update and the value of the attribute they'd like to set.

Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

# for n in new_data:
# new_dict.append(n)

'''
