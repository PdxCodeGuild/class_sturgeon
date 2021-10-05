# mini capstone



import requests

fish_response = requests.get("https://acnhapi.com/v1a/fish")
# name, rarity, location, time, months(northern and southern), shadow size
fish_list = [{fish['name']['name-USen'] : {'rarity' : fish['availability']['rarity'], 'location' : fish['availability']['location'], 'time-array' : fish['availability']['time-array'], 'month-array-northern' : fish['availability']['month-array-northern'], 'month-array-southern' : fish['availability']['month-array-southern'], 'shadow' : fish['shadow']}} for fish in fish_response.json()]
# for fish in fish_list:
#     print(fish, '\n')

sea_creatures_response = requests.get("https://acnhapi.com/v1a/sea")
# name, time, months(northern and southern), speed, shadow size
sea_creatures_list = [{sea['name']['name-USen'] : {'time-array' : sea['availability']['time-array'], 'month-array-northern' : sea['availability']['month-array-northern'], 'month-array-southern' : sea['availability']['month-array-southern'], 'speed' : sea['speed'], 'shadow' : sea['shadow']}} for sea in sea_creatures_response.json()]
# for sea_creature in sea_creatures_list:
#     print(sea_creature, '\n')

bugs_response = requests.get("https://acnhapi.com/v1a/bugs")
# name, rarity, location, time, months(northern and southern)
bugs_list = [{bug['name']['name-USen'] : {'rarity' : bug['availability']['rarity'], 'location' : bug['availability']['location'], 'time-array' : bug['availability']['time-array'], 'month-array-northern' : bug['availability']['month-array-northern'], 'month-array-southern' : bug['availability']['month-array-southern']}} for bug in bugs_response.json()]
# for bug in bugs_list:
#     print(bug, '\n')


