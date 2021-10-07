import requests
import datetime
from statistics import mean
import time
import lenny


def slowprint(text): # print txt slow
    for character in text:
        print(character, end='', flush = True)
        time.sleep(.008)

def address_url_converter(): #Asks user for Address and concatenated it into GoogleMaps URL format
    
    slowprint(f'\n >>>>>>> Lets find the location you want point as the middle of your circle.\n         Please enter the address: (exp - 123 Rocket Rd) \n >>>>>>> ')
    street = input()
    slowprint(f'\n >>>>>>> OK!\n         Now, enter the city (exp - Los Angeles):\n >>>>>>> ')
    city = input()
    slowprint(f'\n >>>>>>> Thanks!\n         Now, enter the state (exp - CA):\n >>>>>>> ')
    state = input()
    
    return str(street.strip().title().replace(' ', '+') + ',+' + city.strip().title().replace(' ', '+') + ',+' + state.strip().upper().replace(' ', '+'))

def lat_log():#Uses address_url_converted to connect with GoogleMaps API, and returns Latitude and Longitude in HNT URL format
    
    while True:
        GoogleMapsKEY = 'AIzaSyC4-KZ9XLmhlZ4GpKMiXC1JCtUiL0ZO6fM'
        GoogleMaps_url = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address_url_converter()}&key={GoogleMapsKEY}')
        GoogleMaps_data = GoogleMaps_url.json()
        try:
            filtered_data = GoogleMaps_data['results'][0]['geometry']['location']
            url_lat_lon = str(f"lat={filtered_data['lat']}&lon={filtered_data['lng']}")
            slowprint("\n\n>>>>>>> GOT IT!!!!  Please wait a little while I search the area... f(ಠ‿↼)z\n ")
            break
        except IndexError:
            slowprint("\n >>>>>>> ಠ▄ಠ Duuuudddeeee!!!!!")
            print(f'''\n\n          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n          ████▌▄▌▄▐▐▌█████\n          ████▌▄▌▄▐▐▌▀████\n          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n\n ''')
            slowprint(f'''>>>>>>> Unfortunatelly GoogleMaps was not able to find the address in the format you enterred... (╯ ͠° ͟ʖ ͡°)╯┻━┻\n         please try again entering the address again, or enter another address closed by the locations.\n"''')

    return url_lat_lon

def get_reward(HotSpot_address): #Takes HotSpot Address in HNT format and returns a list with past rewards
    # HotSpot_addres = '112g66PcozKW84o1cKoZ9PZqhtHzyGgFyJ4B7ZYZ9sZHpQUJXH6e' 
    timeframe = [ 1 , 7 , 30]
    rewards = list()
    
    for days in timeframe:
        
        time = dict()
        time['min_time'] = f'{(datetime.date.today() - datetime.timedelta(days=days))}T00:00:00Z'
        time['max_time'] = f'{(datetime.date.today() + datetime.timedelta(days=1))}T00:00:00Z'
        find_rewards = requests.get(f'https://api.helium.io/v1/hotspots/{HotSpot_address}/rewards/sum', params=time)
        reward_data = find_rewards.json()
        rewards.append(reward_data['data']['total'])

    return rewards

def HotSpots_Data_Finder():# Takes Lat and Log, Ask user for a radius distance, connect with HNY API, returns list with details about each HotStop in the radius
    # lat_log = 'lat=28.4947354&lon=-81.71927'   
    slowprint(f'\n >>>>>>> Lets start by enterting the distance of your search... \n         Please enter the radius distance in --> miles <-- that you would like to the search.\n >>>>>>> How many miles? : ')   
    distance = str(int(float(input()) * 1609.34))

    find_hotspots_url = f'https://api.helium.io/v1/hotspots/location/distance?{lat_log()}&distance={distance}'

    hotspots_url = requests.get(f'{find_hotspots_url}')
    HotSpots_data = hotspots_url.json()
    HotSpots = HotSpots_data['data']

    OrganizedList = list()

    for each_HotSpot in HotSpots:
        HotSpot_name = each_HotSpot['name']
        HotSpot_status = each_HotSpot['status']['online']
        HotSpot_scale = each_HotSpot['reward_scale']
        HotSpot_address = each_HotSpot['address']
        HNT = get_reward(HotSpot_address)

        eactHostSpotDict = {'Name': HotSpot_name.title(), 'Status': HotSpot_status.upper(), 'Reward Scale': HotSpot_scale, '24h' : HNT[0], 'Week' : HNT[1], 'Month' : HNT[2] }

        OrganizedList.append(eactHostSpotDict)

    return OrganizedList

def turn_data_into_csv(data):# Turns data into .CSV 

    title = 'Name, Status, Reward Scale, 24h, Week, Month\n'  #title line
    hotspots_cvs = ''
    linecount = 1

    for index in data:  # loop dictionaries
        for key, value in index.items(): # loop in dictionaries inside the main dictionary 
            hotspots_cvs += str(value) + ', '      # collect on dictionaries value and add a , and turn into a line 
        if linecount < len(data):  # to avoid extra lines on the loop
            hotspots_cvs = hotspots_cvs[:-2]    # remove , from end of the line
            hotspots_cvs += '\n'            # separate lines
            linecount += 1
        
    hotspots_cvs = title + hotspots_cvs[:-2]  # add tittle line and remove last , from last line

    with open('YourSecretHotspotsIntel.csv', "w") as f:
        f.write(hotspots_cvs)
        slowprint("\n >>>>>>> Your file is now saved in your device as 'YourSecretHotspotsIntel.csv'\n ")
    
    return True

def average(data):# Takes data print average and returns answer if user wants to download or not
    # x = [
    #     {'Name': 'Decent-Licorice-Halibut', 'Status': 'ONLINE', 'Reward Scale': 1.0, '24h': 1.00390628, 'Week': 3.0986485, 'Month': 13.32836101}, 
    #     {'Name': 'Cheerful-Champagne-Dragonfly', 'Status': 'ONLINE', 'Reward Scale': 1.0, '24h': 0.2196935, 'Week': 1.27636596, 'Month': 4.81456138}, 
    #     {'Name': 'Innocent-Ash-Ferret', 'Status': 'OFFLINE', 'Reward Scale': 1.0, '24h': 0.51427221, 'Week': 0.8411644, 'Month': 0.8411644}, 
    #     {'Name': 'Clean-Myrtle-Corgi', 'Status': 'ONLINE', 'Reward Scale': 1.0, '24h': 0.01982604, 'Week': 0.01982604, 'Month': 4.33192843}
    #     ]

    ave_24h = list()
    ave_week = list()
    ave_month = list()

    for each in data:
        if each['Status'] == 'ONLINE':
            ave_24h.append(each['24h'])
            ave_week.append(each['Week'])
            if each['Week'] != each['Month']:
                ave_month.append(each['Month'])
            
    slowprint(f'''
        Found {len(ave_24h)} HotSpots currently 'Online' in the area.

        The estimated average rewards 

          ₿    {round(mean(ave_24h), 2)} HNT ₿ in the past 24hs
         ₿₿₿   {round(mean(ave_week), 2)} HNT ₿ in the past 7 days
        ₿₿₿₿₿  {round(mean(ave_month), 2)} HNT ₿ in the past 30 days

        Here are the more details:  ↓            
        ''')

    cc = 0
    for each in data:
        cc += 1
        if each['Status'] == 'OFFLINE':
            slowprint(f"\n    {cc} - {each['Name']} is currently OFFLINE\n\n")
        else:
            print(f"\n    {cc} - {each['Name']} is currently ONLINE with a Reward Scale of {each['Reward Scale']}\n            {round(each['24h'], 2)} HNTs in the past 24h,\n            {round(each['Week'], 2)} HNTs in the past WEEK,\n            {round(each['Month'], 2)} HNTs in the past Month.\n\n")
            time.sleep(0.3)

    slowprint(' >>>>>>> Would you like to download the data in a Excel file?\n      Yes or no ◔_◔ >>>> ')
    answer = input().lower()
    
    if answer == 'yes' or answer == 'y':
        turn_data_into_csv(data)
        return True

    return False

print('''



                                                                    ██╗░░██║░█████║██╗░█████████╗
                                                                    ██║░░██║░██╔██║██║░░░░██╔═══╝
                                                                    ███████║░██║██║██║░░░░██║░░░
                                                                    ██╔══██║░██║██║██║░░░░██║░░░
                                                                    ██║░░██║░██║█████║░░░░██║░░░

                                                                    Welcome to Helium Mini App!!!
                                                                            
                                                                            (▀̿Ĺ̯▀̿) ₿₿₿₿₿₿
''')
slowprint('''                                            This application is designed to find and compare HELIUM HOTSPOTS data in a choosen area
                                          By simplelly entering the the address of the location you wish to seach and radius distance 
                                        You now have access to data of all HNT hotspots you. No more speding hours comparing hexacons!!!
                                                                                                                            
                                                        Find out the best locations for your next HELIUM INVESTMENT 
''')
while True:
    run = average(HotSpots_Data_Finder())
    time.sleep(2)
    loop = str(input('\n >>>>>>> Would you like another search?\n >>>>>>>  '))
    loop = loop.lower()
    if loop == 'no' or loop == 'n':
        break

slowprint('''
>>>>>>>            Thanks for using the Helium Mini App !!!!


                        ░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█ 
                        ░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█ 
                        ░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█ 
                        ░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌ 
                        ░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█ 
                        ▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌ 
                        █▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█ 
                        █▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█ 
                        ▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
                        ▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌
                        █▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐

                                 TO THE MOON

''')