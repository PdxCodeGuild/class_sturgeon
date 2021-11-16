
'''
1.1
Ask the user to enter a mailing address

Street
City
State
Zip Code

Assign the value of each field to a variable

Display the address back to the user using an f-string

Enter street: 231 Faux Ave.
Enter city: Portland
Enter state: Oregon
Enter zip code: 97211

Output:
231 Faux Ave.
Portland, Oregon
97211
1.2
Using string methods, ensure that the address will be properly capitalized, no matter how it's entered.

'''

street = input('Enter street: ')
city = input('Enter city: ')
state = input('Enter state: ')
zip = input('Enter zip code: ')

street = street.title()
city = city.title()
state = state.upper()


print(f'{street} \n{city}, {state} \n{zip}')

