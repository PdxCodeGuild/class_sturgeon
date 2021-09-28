import re
#Opens CSV file
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

#Final Contact list
contact_list_complete = []    

#Splits list, uses for loors to create dict's and appens to final list
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


