import re

with open('practice.csv' , 'r') as file:
    lines = file.read().split('\n')

contacts = []
keys_list = re.split(',', lines[0])

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
    
print(contacts)


