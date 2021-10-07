import yfinance as yf
import requests
#import yahoo_fin.stock_info as si
import pandas as pd
import json

ticker = input("Input ticker symbol: ").upper()

data = yf.Ticker(ticker)

print(data.info).json()

'''
# analysis
response = requests.get("https://yh-finance.p.rapidapi.com/stock/v2/get-analysis", headers={
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
}, params={"symbol": ticker, "region": "US"}).json()

print(response)



url = "https://yh-finance.p.rapidapi.com/news/v2/list"

querystring = {"region": "US", "snippetCount": "28", "s": ticker}

payload = "\"Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page\""
headers = {
    'content-type': "text/plain",
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
}

response = requests.request(
    "POST", url, data=payload, headers=headers, params=querystring).json()

print(response)
'''
