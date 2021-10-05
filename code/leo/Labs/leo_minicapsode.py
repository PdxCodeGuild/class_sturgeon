import requests


theresponse = requests.get('https://api.helium.io/v1/hotspots/location/distance?lat=28.4949085558503&lon=-81.71925853438259&distance=3000')

print(theresponse)
x = theresponse.json()

print(f'\n {x} \n')