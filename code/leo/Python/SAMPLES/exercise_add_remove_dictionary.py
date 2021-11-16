
fruits = {
    'apple' : 0.65, 
    'banana' : 0.5, 
    'guava' : 0.33, 
    }

print(f"Apples cost ${fruits['apple']} each")

fruits['grapes'] = 0.99
print(f"Added 'grapes': {fruits}")

fruits.pop('banana')
print(f"Removed 'banana': {fruits}")
