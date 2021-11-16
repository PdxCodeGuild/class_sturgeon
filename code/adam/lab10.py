# Lab 10: Contact List
import time

csv_folder = 'contacts.csv'
print("")
with open(csv_folder, 'r') as f:
    lines = f.read().split('\n')
    for i in range(len(lines)):
        #Break up the big list into smaller lists
        lines[i] = lines[i].split(',')

#make a list of dictionaries using a function that inputs the above 'lines' variable
contacts = []
def list_maker(my_row):
    for i in range(1,len(my_row)):
    #force the lists into a dictionary by adding {my_row:my_row} method
        contacts.append({
            my_row[0][0]: my_row[i][0], #Name
            my_row[0][1]: my_row[i][1], #Relationship Status
            my_row[0][2]: my_row[i][2], #Kids?
            my_row[0][3]: my_row[i][3]  #State
        })
    return contacts

list_maker(lines)

#Version 2, Part 1: Create: Ask for user input and make another contact in the list
new_person = ""
def new_contact():
    value4_0 = input("Enter your first name:-->")
    value4_1 = input("Enter your relationships status (ie married, single, etc):-->")
    value4_2 = input("Do you have any children?-->")
    value4_3 = input("What state do you reside in?-->")
    global new_person
    new_person = value4_0
    contacts.append({
    lines[0][0]: value4_0, #Name
    lines[0][1]: value4_1, #Relationship Status
    lines[0][2]: value4_2, #Children?
    lines[0][3]: value4_3  #State
})

# new_contact()

#Version 2, Part 2: Retrieve: ask user for contact's name, find it, display information
# query = input("Whom are you searching for?-->")

query_result = ""
#Merritt is awesome
def find_user():
    while True:
        query = input("Enter Name:-->")
        for contact in contacts:
            if contact["name"] == query:
                global query_result
                query_result = contact
                return query_result
        answer = input("Name not found. Try again? (y/n)-->").lower()
        if answer == 'n':
            break

# find_user()
# print(query_result)

#Version 2, Part 3: Update: ask user for contact's name, find the attribute they want to update, and the value of the attribute to set
def user_update():
    find_user()
    while True:
        key_to_update = input("What would you like to update? (name(n) relationship status(r) children (c) state (s))-->").lower()
        if key_to_update == "n":
            value_to_update = input("Enter updated name:-->")
            query_result["name"] = value_to_update
            break
        if key_to_update == "r":
            value_to_update = input("Enter updated relationship status:-->")
            query_result["relationship status"] = value_to_update
            break
        if key_to_update == "c":
            value_to_update = input("Enter updated children status (yes/no):-->")
            query_result["kids (yes/no)"] = value_to_update
            break
        if key_to_update == "s":
            value_to_update = input("Enter updated state:-->")
            query_result["state"] = value_to_update
            break
        else:
            print("Your choice was not recognized")
            continue

# user_update()
# print(contacts)

#Version 2, Part 4: Delete: ask user for contact's name, remove the contact from the list
bye_user = ""
def del_user():
    bye = input("Enter Name to be removed:-->")
    global bye_user
    bye_user = bye 
    for i in range(len(contacts)):
        if contacts[i]['name'] == bye:
            print(f'{bye} is being deleted from the Database...')
            time.sleep(1)
            print(f'{bye} has been deleted')
            del contacts[i]
            break
    else:
        print("User not Found")

# del_user()
# print(contacts)
header = contacts[0]
def save(contacts, csv_folder, header):
    lines = [','.join(header)] #Put 'em back together
    for contact in contacts: #Loop through the contacts, just like searching
        row = ','.join(contact.values()) #Make the values in contact actually be separated by commas
        lines.append(row)  #Put each line in a row

    csv_string = '\n'.join(lines) #Need this to make the lines list a string again

    with open(csv_folder, 'w') as f: #Doing the 'w' instead of 'r' so we can write and using 'f:' instead of file as per Merritt's suggestion in class
        f.write(csv_string)

#Run the CRUD
while True:
    crud = input("Welcome to the Library-Interface Database. Username: New(N) Lookup(L) Update(U) Delete(D) or Quit(Q):-->").upper()
    if crud == "N":
        new_contact()
        print(f'{new_person} has been added to the database')
        time.sleep(1.5)
        save(contacts, csv_folder, header)
    elif crud == "L":
        find_user()
        time.sleep(1)
        print(query_result)
        save(contacts, csv_folder, header)
    elif crud == "U":
        user_update()
        time.sleep(1)
        print(contacts)
        save(contacts, csv_folder, header)
    elif crud == "D":
        del_user()
        time.sleep(1.5)
        save(contacts, csv_folder, header)
    elif crud == "Q":
        break
    else:
        print("Incorrect entry. Try Again.")
        continue

print("Thank you for using the Library-Interface Database")


''' A backup of the initial csv information
name,relationship status,kids (yes/no),state
adam,single,no,utah
erin,single,no,florida
ean,single,no,idaho
'''