'''
#analysis
response = requests.get("https://yh-finance.p.rapidapi.com/stock/v2/get-analysis", headers={
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
}, params={"symbol": ticker, "region": "US"}).json()

print(response)

#news
import requests

url = "https://yh-finance.p.rapidapi.com/news/v2/get-details"

querystring = {"uuid":"9803606d-a324-3864-83a8-2bd621e6ccbd","region":"US"}

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

'''
