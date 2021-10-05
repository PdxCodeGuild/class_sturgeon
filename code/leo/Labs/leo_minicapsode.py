import requests

def address_url_converter(): #asks user for US address and concatenated it into GoogleMaps URL format
    street = input(f' Please enter the address:\n>>>>>>> ')
    city = input(f' \nPlease enter the city:\n>>>>>>> ')
    state = input(f' \nPlease enter the 2 letter state:\n>>>>>>> ')
    
    return str(street.strip().title().replace(' ', '+') + ',+' + city.strip().title().replace(' ', '+') + ',+' + state.strip().upper().replace(' ', '+'))

def lat_log():
    
    while True:
        # MapQuestKEY = '5TbsKqN9vG810Qy5ckoUVcALAGKrurVm'
        GoogleMapsKEY = 'AIzaSyC4-KZ9XLmhlZ4GpKMiXC1JCtUiL0ZO6fM'
        GoogleMaps_url = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address_url_converter()}&key={GoogleMapsKEY}')
        GoogleMaps_data = GoogleMaps_url.json()
        try:
            filtered_data = GoogleMaps_data['results'][0]['geometry']['location']
            url_lat_lon = str(f"lat={filtered_data['lat']}&lon={filtered_data['lng']}")
            break
        except IndexError:
            print("\nUnfortunatelly GoogleMaps was not able to find the address in this format... -__-\n please try again, or enter another address in the same locations.\n")

    return url_lat_lon

def hotspot_finder():

    distance = str(int(float(input(f'\nPlease enter the miles radius you would like to search.\n>>>>> how many miles : ')) * 1609.34))

    find_hotspots_url = f'https://api.helium.io/v1/hotspots/location/distance?{lat_log()}&distance={distance}'

    hotspots_url = requests.get(f'{find_hotspots_url}')
    HotSpots_data = hotspots_url.json()

    Hotspot_name = HotSpots_data['data'][0]['name']
    Hotspot_status = HotSpots_data['data'][0]['status']['online']
    Hotspot_scale = HotSpots_data['data'][0]['reward_scale']
    Hotspot_address = HotSpots_data['data'][0]['address']
    
    done = f'In your area we found {Hotspot_name} that is currently {Hotspot_status} and is makeing {Hotspot_scale} in the address {Hotspot_address}'
    return done



# # paramss={'name':'decent-licorice-halibut'}
#     # '112g66PcozKW84o1cKoZ9PZqhtHzyGgFyJ4B7ZYZ9sZHpQUJXH6e' : 'address'
#     # 'max_time': '2021-10-04T00:00:00Z',
#     # 'min_time': '2021-10-03T00:00:00Z',

# yep={'min_time': '2021-07-05T00:00:00Z','max_time': '2021-09-01T00:00:00Z'}


# theresponse = requests.get(f'https://api.helium.io/v1/hotspots/112g66PcozKW84o1cKoZ9PZqhtHzyGgFyJ4B7ZYZ9sZHpQUJXH6e/rewards/sum', params=yep)

# print(theresponse)
# x = theresponse.json()

# print(f'\n {x} \n')