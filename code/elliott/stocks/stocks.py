import requests
import yfinance as yf
import yahoo_fin.stock_info as si


#------------------------------------------------------API----------------------------------------------------------#


def rec(ticker):
    x = yf.Ticker(ticker)
    print(x.recommendations)


def news(ticker, limit):
    poly_api_key = "2d5b7LFFuTGUowh3lmLW8M_pFQbDNmx3"
    url = f"https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&apiKey={poly_api_key}"
    news = requests.get(url).json()
    print(news)


def finacials(ticker):
    quote_table = si.get_quote_table(ticker, dict_result=False)
    pe_ratio = quote_table
    print(pe_ratio)
    income_statement = si.get_income_statement(ticker)
    print(income_statement)


def analysis(ticker):
    analysis = requests.get("https://yh-finance.p.rapidapi.com/stock/v2/get-analysis", headers={
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "3626506961msh6043bed195d39acp11b912jsna00bcc337f5c"}, params={"symbol": ticker, "region": "US"}).json()
    buy_sell = analysis['financialData']['recommendationKey']
    cash_flow = analysis['financialData']['freeCashflow']['fmt']
    fifty_two_weekHigh = analysis['summaryDetail']['fiftyTwoWeekHigh']['fmt']
    debt_to_equity = analysis['financialData']['debtToEquity']['fmt']
    previous_price = analysis['price']['regularMarketPreviousClose']['fmt']

    print(f"""
    These are our reccomendations based on the fundamental analysis: 
    --------------------------------------------------------------------
    
    {ticker}'s previous closing price was ${previous_price}. With a 52 week high of ${fifty_two_weekHigh}. 
    Expert analysis has it rated as a {buy_sell}. 

    Important metics:
    Cash flow (+/-): {cash_flow} 
    Debt to equity: {debt_to_equity}

    --------------------------------------------------------------------
     > """)
#-------------------------------------------------------API---------------------------------------------------------------#


#----------------------------------------------------user promps----------------------------------------------------------#
def promp():
    choice = input("""
    Enter one of the options below or 'All' for full fundamental report.
    --------------------------------------------------------------------
      1. News
      2. Analysis [...]
      3. Reccomendations
      4. All
      5. Exit
    --------------------------------------------------------------------
     > """).lower()
    return choice


def promp2():
    choice2 = input("""
    Enter one of the options below or 'back' to return to last page.
    --------------------------------------------------------------------
    1.finacials
    2.expert buy/sell
    3.back

    --------------------------------------------------------------------
     > """).lower()
    return choice2


def promp3():
    choice3 = input("""
    1. Back
    2. Exit
     > """).lower()
    return choice3
#----------------------------------------------------user promps----------------------------------------------------------#


ticker = input("Input ticker symbol: ").upper()
# choice = promp()
while True:
    choice = promp()
    if choice == "1":
        limit = input(f"How many news articles related to {ticker}?  ")
        news(ticker, limit)
    elif choice == "2":
        while True:
            choice2 = promp2()
            if choice2 == "1":
                finacials(ticker)
            elif choice2 == "2":
                rec(ticker)
            elif choice2 == "3":
                break
    elif choice == "3":
        analysis(ticker)
        while True:
            choice3 = promp3()
            if choice3 == "1":
                break
            elif choice3 == "2":
                quit()
    elif choice == "4":
        rec(ticker),
        analysis(ticker)
        news(ticker, '5')
    elif choice == "5":
        break
    else:
        print(f'{choice} is not a option. ')
        break
