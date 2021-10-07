# mini capstone
# animal crossing critter logging companion



import requests
import pygal
import webbrowser


def all_critters (critter_list):
    return [''.join(critter.keys()) for critter in critter_list]
  



def new_critter (user_input, inventory_list):
    inventory_list.append(user_input)


def my_critters (inventory_list):
    for critter in inventory_list:
        print(critter, '\n')

def remaining_critters (inventory_list, critter_list):
    remaining_critters = [critter for critter in critter_list if critter not in inventory_list]
    return remaining_critters

def pie_chart (inventory_list, critter_list, section):
    pie_chart = pygal.Pie()
    pie_chart.title = f'Caught {section} vs. uncaught {section}'
    pie_chart.add('Caught', len(inventory_list))
    pie_chart.add('Uncaught', len(remaining_critters(inventory_list, critter_list)))
    pie_chart.render_to_file('file.svg')
    url = 'file.svg'
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)



fish_response = requests.get("https://acnhapi.com/v1a/fish")
#print(fish_response.json())
# name, rarity, location, time, months(northern and southern), shadow size
fish_list = [{fish['name']['name-USen'] : {'rarity' : fish['availability']['rarity'], 'location' : fish['availability']['location'], 'time-array' : fish['availability']['time-array'], 'month-array-northern' : fish['availability']['month-array-northern'], 'month-array-southern' : fish['availability']['month-array-southern'], 'shadow' : fish['shadow']}} for fish in fish_response.json()]


sea_creatures_response = requests.get("https://acnhapi.com/v1a/sea")
# name, time, months(northern and southern), speed, shadow size
sea_creatures_list = [{sea['name']['name-USen'] : {'time-array' : sea['availability']['time-array'], 'month-array-northern' : sea['availability']['month-array-northern'], 'month-array-southern' : sea['availability']['month-array-southern'], 'speed' : sea['speed'], 'shadow' : sea['shadow']}} for sea in sea_creatures_response.json()]


bugs_response = requests.get("https://acnhapi.com/v1a/bugs")
# name, rarity, location, time, months(northern and southern)
bugs_list = [{bug['name']['name-USen'] : {'rarity' : bug['availability']['rarity'], 'location' : bug['availability']['location'], 'time-array' : bug['availability']['time-array'], 'month-array-northern' : bug['availability']['month-array-northern'], 'month-array-southern' : bug['availability']['month-array-southern']}} for bug in bugs_response.json()]



fish_inventory = []
sea_creatures_inventory = []
bugs_inventory = []


critter_encylcopedia = {
    'fish' : fish_list,
    'sea creatures' : sea_creatures_list,
    'bugs' : bugs_list
}
user_inventories = {
    'fish' : fish_inventory,
    'sea creatures' : sea_creatures_inventory,
    'bugs' : bugs_inventory
}


# begin program
print('Welcome to the Animal Crossing Critter Catching Companion!')
while True:
    section = input("What section are you interested in working on today?\nEnter 'fish', 'sea creatures', 'bugs', or 'exit'\n")
    if section == 'exit':
        print('Goodbye')
        break
    
    elif section in list(critter_encylcopedia.keys()):
        command = input(f"""
What would you like to do?
    'list' = see all {section} available
    'new' = enter new {section} into your inventory
    'inventory' = see your {section} inventory
    'uncaught' = see what {section} you have left to catch
    'chart' = see caught vs uncaught {section} chart
        """)
        if command == 'list':
            for critter in all_critters(critter_encylcopedia[section]):
                print(critter)

        if command == 'new':
            while True:
                user_critter = input(f"Enter what you caught:\n").lower()
                if user_critter in all_critters(critter_encylcopedia[section]):

                    new_critter (user_critter, user_inventories[section])
                    print(user_inventories[section])
                    another = input("Would you like to make another entry? 'yes' or 'no'\n")
                    if another != 'yes':
                        break
                else:
                    print(f'That entry is not in the {section} list')
        if command == 'inventory':
            if user_inventories[section] == []:
                print("Your inventory is empty")
            else:
                for critter in user_inventories[section]:
                    print(critter)
        if command == 'uncaught':
            for critter in remaining_critters (user_inventories[section], all_critters(critter_encylcopedia[section])):
                print(critter)
        if command == 'chart':
            pie_chart(user_inventories[section], all_critters(critter_encylcopedia[section]), section)
        elif command != ['list', 'new', 'inventory', 'uncaught', 'chart']:
            print('Entry not recognized')
    else:
        print('Entry not recognized')



# add while true on line 84? change if statements to elif and else
# work on datetime? use data to see if anything is avaiable to catch
