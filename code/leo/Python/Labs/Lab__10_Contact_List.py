
def turns_csv_into_dictionary(file): #take a cvs file and turn into a main dictionary with dictionaries inside. Each user is a dictionary where the key is category and value the dogs data.
    with open(file, 'r') as dog:
        dogs = dog.read().split('\n')

    dog_info = []
    for x in dogs: 
        dog_info.append(x.split(', '))
    dictionary = [{'name': i[0], 'breed': i[1], 'sex': i[2], 'age': i[3]} for i in dog_info]
    # turn list into dictionary, each dog's ifo becomes a dictionary that used they type of data as key for the dogs information.  
    dictionary.remove({'name': 'name', 'breed': 'breed', 'sex': 'sex', 'age': 'age'}) 
    # I need to revome header, decided to remove here instead of conditional statment. 
    return dictionary

def create_new_record(dictionary): #add dictionary to main dictionary

    name = input("Please enter the dog's name: ").title()
    breed = input("Please enter the dog's breed: ").lower()
    sex = input("Please enter the dog's sex: ").lower()
    age = input("Please enter the dog's age: ")
    new_dog = {'name': name, 'breed': breed, 'sex': sex, 'age': age}
    
    return dictionary.append(new_dog)
    
def find_record(dictionary): #find record and return string

    name = input("Please enter the dog's name: ").title() #find a key

    for x in dictionary: # loop the dictionary
        if name == x['name']: # if key in dictionary add values to variables
            dogs_name = x['name']
            dogs_breed = x['breed']
            dogs_sex = x['sex']
            dogs_age = x['age']
            found = f"{dogs_name} is a {dogs_sex} {dogs_breed} at the age of {dogs_age}." #return string with variables
            break
        else:
            found = f'Dog not found!' #return if key invalid.

    return found 

def update_record(dictionary): # update record inside dictionary

    name = input("Please enter the name of dog you would like to update : ").title() # find a key
    
    for x in dictionary: # loop the dictionary with user's input 
        
        if name == x['name']: # verity if key is in the dictionary.
            dictionary.remove(x) # delete old record with key
            name = input("Please enter the dog's name: ").title()        #create a new record with same key
            breed = input("Please enter the dog's breed: ").lower()
            sex = input("Please enter the dog's sex: ").lower()
            age = input("Please enter the dog's age: ")
            new_dog = {'name': name, 'breed': breed, 'sex': sex, 'age': age} # use data to create a new dictionary
            return dictionary.append(new_dog)   # add new dictionary to main dictionary
        
    else:
        return 'Dog not found!' # return if key not found

def delete_record(dictionary):

    name = input("Please enter the name of dog you would like to delete from your list : ").title()
    
    for x in dictionary:
        
        if name == x['name']:
    
            return dictionary.remove(x)
        
    else:
        return 'Dog not found!'

def turns_dictionary_into_csv(dictionary): #turns a dictionary into a cvs format string
    
    title = 'name, breed, sex, age\n'  #title line
    dogs_cvs = ''
    linecount = 1

    for index in dictionary:  # loop dictionaries
        for key, value in index.items(): # loop in dictionaries inside the main dictionary 
            dogs_cvs += value + ', '      # collect on dictionaries value and add a , and turn into a line 
        if linecount < len(dictionary):  # to avoid extra lines on the loop
            dogs_cvs = dogs_cvs[:-2]    # remove , from end of the line
            dogs_cvs += '\n'            # separate lines
            linecount += 1
    
    dogs_cvs = title + dogs_cvs[:-2]  # add tittle line and remove last , from last line
    
    return dogs_cvs  #return string in the cvs format

user = True

choice_of_file = input('''
        Hello!!!  Welcome to Doggie Data! 
Please enter the "file.cvs" you would like access!
>>>>>> : ''')
dictionary = turns_csv_into_dictionary(choice_of_file)

while user == True:   # loop MENU until user save and exit

    menu_choice = input(''' 
    MENU :

    enter "FIND" to see lookup for a dog's data on file;
    enter "ADD" to add a new dog into the file;
    enter "UPDATE" to add update a dog's data on file;
    enter "REMOVE" to revome a dog's data from the file;

    or enter "SAVE" to save changes and exit program;

   ''').upper()

    if menu_choice == 'FIND': #find a dog, loop unitl user decise to exit it.
        question = 'YES'
        while question == 'YES':
            print(find_record(dictionary))
            question = input('\nWould you like to find data on another dog? ').upper()

    elif menu_choice == 'ADD': #add dog, loop unitl user decise to exit it.
        question = 'YES'
        while question == 'YES':
            print(create_new_record(dictionary))
            question = input('\nWould you like to add another dog? ').upper()
    
    elif menu_choice == 'UPDATE': #update dog, loop unitl user decise to exit it.
        question = 'YES'
        while question == 'YES':
            print(update_record(dictionary))
            question = input('\nWould you like to update data on another dog? ').upper() 
    
    elif menu_choice == 'REMOVE': #update dog, loop unitl user decise to exit it.
        question = 'YES'
        while question == 'YES':
            print(delete_record(dictionary))
            question = input('\nWould you like to delete data of another dog? ').upper() 
          
    elif menu_choice == 'SAVE':
        question = input(f'\nWould you like to save changes in the same file "{choice_of_file}" ? ').upper()
        
        if question == 'YES':
            with open(choice_of_file, "w") as f:
                f.write(turns_dictionary_into_csv(dictionary))
            print(f'\n Your file has been saved as "{choice_of_file}" \n Good Bye!!!')
            user = False
        
        else:
            newfile = input('\nPlease enter the name of the new .CSV file: ')
            with open(newfile, "w") as f:
                f.write(turns_dictionary_into_csv(dictionary))
            print(f'\n Your file has been saved as "{newfile}" \n Good Bye!!!')
            user = False
