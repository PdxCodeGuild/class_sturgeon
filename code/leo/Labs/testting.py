dogs = [{'name': 'Bobby', 'breed': 'pug', 'sex': 'male', 'age': '1'}, 
{'name': 'Bella', 'breed': 'golden retriever', 'sex': 'female', 'age': '2'}, 
{'name': 'Milo', 'breed': 'chihuahua', 'sex': 'male', 'age': '5'}, 
{'name': 'Selma', 'breed': 'pekingese', 'sex': 'female', 'age': '3'}, 
{'name': 'Keke', 'breed': 'shiba', 'sex': 'male', 'age': '5'}
]

print(dogs)

', '.join(f'{k}_{v}' for k, v in dogs.items())

print(x)