# mini capstone
# animal crossing critter logging companion



import requests

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



def all_critters (critter_list):
    for critter in critter_list:
        print(critter, '\n')


fish_inventory = []
sea_creatures_inventory = []
bugs_inventory = []
def new_critter (user_input, inventory_list):
    # remove added critter from master list
    # fish_list.remove(user_input)
    inventory_list.append(user_input)

def my_critters (inventory_list):
    for critter in inventory_list:
        print(critter, '\n')

def remaining_critters (inventory_list, critter_list):
    remaining_critters = [critter for critter in critter_list if critter not in inventory_list]
    return remaining_critters
    # returns fish_list

     
all_critters(fish_list)
# print(remaining_critters(fish_inventory, fish_list))
# new_critter('barreleye', fish_inventory)
# print(fish_list)

# master list of all fish, etc. names in a list remove item from master list when adding that item to user inventory list
# new var named simple list
# try a dict :)
