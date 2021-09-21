
import csv

with open('contacts.csv', 'r') as file:
    lines = file.read(name).split(\n)
    lines = file.read(favorite_fruit).split(\n)
    lines = file.read(favorite_color).split(\n)
    print(lines)


'''

Let's build a program to manage a list of contacts. To start, we'll build a CSV 
('comma separated values') together, and go over how to load that file. 
Headers might consist of name, favorite fruit, favorite color. Open the CSV, 
convert the lines of text into a list of dictionaries, one dictionary for each user. 
The text in the header represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.

'''
