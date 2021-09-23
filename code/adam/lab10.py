# Lab 10: Contact List

#method 1
# print("")
# contacts = {}
# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     # print(lines)
#     for line in lines:
#         (key, *val) = line.split(",")
#         contacts[key] = val
# print(contacts)

# def merge(dict1, dict2):
#     res = dict1 | dict2
#     return res

# merge(contacts['name'], contacts['adam'])


# This makes: {'name': ['relationship status', 'kids (yes/no)', 'state'], 'adam': ['single', 'no', 'utah'], 'erin': ['single', 'no', 'florida']}

#method 2
#Load csv data into a string variable
# with open('contacts.csv', 'r') as f:
#     contacts_list = [[val.strip() for val in r.split(",")] for r in f.readlines()] 
#     #Create a list of each row by splitting it and getting rid of the \n with .split("\n") 
#     #Get rid of the \n in the dictionary by also using .strip()
#     #Readlines() is used to read all the lines at a single go and then return them as each line a string element in a list. 

# print("")

# #Create the dictionary
# contacts_dict = {}

# (_, *header), *data = contacts_list
# #This (_, *header) line makes it so instead of {'name': {...}} it reads {'adam': {...}} initially and creates a header
# #the '*' next to the header and data keeps it from complaining about unpacking too many values (expected 2)
# for row in data:
#     key, *values = row
#     contacts_dict[key] = {key: value for key, value in zip(header, values)}

# print(contacts_dict)
# print(type(contacts_dict))
# print(contacts_dict["adam"])
# print(f"Contacts = {list(contacts_list.items())}")

#method 3
from ast import Index


print("")
with open('contacts.csv', 'r') as f:
    lines = f.read().split('\n')
    # print(lines)
    for i in range(len(lines)):
        #Break up the big list into smaller lists
        lines[i] = lines[i].split(',')
    # print(lines)
# print("")

contacts = []
for i in range(1,len(lines)):
    #force the lists into a dictionary by adding {lines:lines} method
    contacts.append({
        lines[0][0]: lines[i][0], #Name
        lines[0][1]: lines[i][1], #Relationship Status
        lines[0][2]: lines[i][2], #Kids?
        lines[0][3]: lines[i][3]  #State
    })

print("")
print(contacts)
print(type(contacts))
#Version 2, Part 1: Ask for user input and make another contact in the list
# value4_0 = input("Enter your first name:-->")
# value4_1 = input("Enter your relationships status (ie married, single, etc):-->")
# value4_2 = input("Do you have any children?-->")
# value4_3 = input("What state do you reside in?-->")
# contacts.append({
#     lines[0][0]: value4_0,
#     lines[0][1]: value4_1,
#     lines[0][2]: value4_2,
#     lines[0][3]: value4_3
# })

# print("")
# print(contacts)

#Version 2, Part 2: Ask user for contact's name, find the name, and display their information

a_key = "name"
values_of_key = [a_dict[a_key] for a_dict in contacts]
print(values_of_key) #['adam', 'erin', 'ephraim']

query = input("What name are you looking for?-->")
# if query in contacts:
#     print("yep")

#Merritt is awesome
for contact in contacts:
    if contact["name"] == query:
        print(contact)

# print(query)

# if contacts["name" == "adam"] in contacts[0]:
#     print("It's in the first one")
# if query in contacts[1]:
#     print("It's in the second one")
# if query in contacts[2]:
#     print("It's in the third one")

# for item in contacts:
#     if  "name" in item:
#         print("yahoo")


# if query in values_of_key:
#     print("found it")
    # print(contacts[0])
    # print(dict(contacts["name":query])
    # print(contacts["name":query])
    # print(values_of_key[query])
    # print(dict(contacts["adam"]))
    # print(contacts.get("names", query))


''' so far we're getting:
method 1:
{'name': ['relationship status', 'kids (yes/no)', 'state'], 'adam': ['single', 'no', 'utah'], 'erin': ['single', 'no', 'florida']}
method 2:
{'adam': {'relationship status': 'single', 'kids (yes/no)': 'no', 'state': 'utah'}, 'erin': {'relationship status': 'single', 'kids (yes/no)': 'no', 'state': 'florida'}}
method 3: This works
[{'name': 'adam', 'relationship status': 'single', 'kids (yes/no)': 'no', 'state': 'utah'}, 
    {'name': 'erin', 'relationship status': 'single', 'kids (yes/no)': 'no', 'state': 'florida'}, 
    {'name': 'ephraim', 'relationship status': 'married', 'kids (yes/no)': 'no', 'state': 'idaho'}]
'''

''' example from lab10
contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
'''


''' A backup of the initial csv information
name,relationship status,kids (yes/no),state
adam,single,no,utah
erin,single,no,florida
ean,single,no,idaho
'''