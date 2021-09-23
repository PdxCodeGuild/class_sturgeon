dogs_dictionary = [{'name': 'Bobby', 'breed': 'pug', 'sex': 'male', 'age': '1'}, 
{'name': 'Bella', 'breed': 'golden retriever', 'sex': 'female', 'age': '2'}, 
{'name': 'Milo', 'breed': 'chihuahua', 'sex': 'male', 'age': '5'}, 
{'name': 'Selma', 'breed': 'pekingese', 'sex': 'female', 'age': '3'}, 
{'name': 'Keke', 'breed': 'shiba', 'sex': 'male', 'age': '5'}
]

def create_new_record():

    name = input("Please enter the dog's name: ").title()
    breed = input("Please enter the dog's breed: ").lower()
    sex = input("Please enter the dog's sex: ").lower()
    age = input("Please enter the dog's age: ")
    new_dog = {'name': name, 'breed': breed, 'sex': sex, 'age': age}
    
    return dogs_dictionary.append(new_dog)
    
def find_record():

    name = input("Please enter the dog's name: ").title()

    for x in dogs_dictionary:
        if name == x['name']:
            dogs_name = x['name']
            dogs_breed = x['breed']
            dogs_sex = x['sex']
            dogs_age = x['age']
            found = f"{dogs_name} is a {dogs_sex} {dogs_breed} at the age of {dogs_age}."
            break
        else:
            found = f'Dog not found!'

    return found 

def update_record():

    name = input("Please enter the name of dog you would like to update : ").title()
    
    for x in dogs_dictionary:
        
        if name == x['name']:
            dogs_dictionary.remove(x)
            name = input("Please enter the dog's name: ").title()
            breed = input("Please enter the dog's breed: ").lower()
            sex = input("Please enter the dog's sex: ").lower()
            age = input("Please enter the dog's age: ")
            new_dog = {'name': name, 'breed': breed, 'sex': sex, 'age': age}
            dogs_dictionary.append(new_dog)
            return dogs_dictionary
        
        else:
            return 'Dog not found!'

def delete_record():

    name = input("Please enter the name of dog you would like to delete from your list : ").title()
    
    for x in dogs_dictionary:
        
        if name == x['name']:
            dogs_dictionary.remove(x)
            return dogs_dictionary
        
        else:
            return 'Dog not found!'


with open("contacts2.cvs", "w") as f:
    f.write(dogs_dictionary)