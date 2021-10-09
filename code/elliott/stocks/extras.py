import requests
import yfinance as yf
from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si


ticker = input(">")

'''
def finacials(ticker):
    quote_table = si.get_quote_table(ticker, dict_result=False)
    pe_ratio = quote_table
    print(pe_ratio)
    income_statement = si.get_income_statement(ticker)
    print(income_statement)
'''


def analysis(ticker):
    analysis = requests.get("https://yh-finance.p.rapidapi.com/stock/v2/get-analysis", headers={
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"}, params={"symbol": ticker, "region": "US"}).json()
    buy_sell = analysis['financialData']['recommendationKey']
    cash_flow = analysis['financialData']['freeCashflow']['fmt']
    fifty_two_weekHigh = analysis['summaryDetail']['fiftyTwoWeekHigh']['fmt']
    debt_to_equity = analysis['financialData']['debtToEquity']
    previous_price = analysis['price']['regularMarketPreviousClose']
    print(f"""
    These are our reccomendations based on the fundamental analysis:
    --------------------------------------------------------------------
    {cash_flow}
    {fifty_two_weekHigh}
    {debt_to_equity}
    {buy_sell}




    3.back
    --------------------------------------------------------------------
     > """).lower()





""")


analysis(ticker)


'''
def analysis(ticker):
    print(f" The anaylis for today is ..... {ticker}")


def news(ticker, limit):
    print(f" The news for today is ..... {ticker}")


def earnings(ticker):
    print(f" The earnings for today is ..... {ticker}")

     EARNINGS PER SHARE(EPS)


PRICE TO EARNINGS RATIO(P/E)
PROJECTED EARNINGS GROWTH(PEG)
. FREE CASH FLOW(FCF)
PRICE TO BOOK RATIO(P/B)
RETURN ON EQUITY(ROE)
DIVIDEND PAYOUT RATIO(DPR)
 PRICE TO SALES RATIO(P/S)
 DIVIDEND YIELD RATIO
 DEBT-TO-EQUITY RATIO(D/E)


ticker = input("Input ticker symbol: ").upper()
# PRICE TO EARNINGS RATIO (P/E)
quote_table = si.get_quote_table(ticker, dict_result=False)
pe_ratio = quote_table

print(pe_ratio)

income_statement = si.get_income_statement(ticker)
print(income_statement)
'''
'''
# analysis
response = requests.get("https://yh-finance.p.rapidapi.com/stock/v2/get-analysis", headers={
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
}, params={"symbol": ticker, "region": "US"}).json()

print(response)

# news
import requests

url = "https://yh-finance.p.rapidapi.com/news/v2/get-details"

querystring = {"uuid":"9803606d-a324-3864-83a8-2bd621e6ccbd","region":"US"}

headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)







#------------------------------------------------------------------------------------------------#
 EARNINGS PER SHARE (EPS)
PRICE TO EARNINGS RATIO (P/E)
PROJECTED EARNINGS GROWTH (PEG)
. FREE CASH FLOW (FCF)
PRICE TO BOOK RATIO (P/B)
RETURN ON EQUITY (ROE)
DIVIDEND PAYOUT RATIO (DPR)
 PRICE TO SALES RATIO (P/S)
 DIVIDEND YIELD RATIO
 DEBT-TO-EQUITY RATIO (D/E)
#------------------------------------------------------------------------------------------------#


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





# data = yf.Ticker(ticker)
# print(data.info)

#------------------------------------------------------------------------------------------------#
t12_api_key = "00854453c7a841729c6197f1074e8bce"
rapidapi_key = "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"
poly_api_key = "2d5b7LFFuTGUowh3lmLW8M_pFQbDNmx3"
#------------------------------------------------------------------------------------------------#

'''
