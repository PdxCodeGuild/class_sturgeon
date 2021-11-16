import requests
import yfinance as yf
import yahoo_fin.stock_info as si
from yahoo_fin.stock_info import get_data
import plotly.graph_objects as go

#---------------------------------------------API----------------------------------------------------------#


def rec(ticker):
    x = yf.Ticker(ticker)
    print(x.recommendations)


def news(ticker, limit):
    poly_api_key = "2d5b7LFFuTGUowh3lmLW8M_pFQbDNmx3"
    url = f"https://api.polygon.io/v2/reference/news?limit={limit}&order=descending&sort=published_utc&ticker={ticker}&apiKey={poly_api_key}"
    news = requests.get(url).json()
    title = news['results'][0]['title']
    author = news['results'][0]['author']
    news_url = news['results'][0]['article_url']
    print(f"""
    Title: {title}
    
    Author: {author}

    Url: {news_url}
    

    """)


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
    returnOnEquity = analysis["financialData"]["returnOnEquity"]['fmt']
    targetMeanPrice = analysis['financialData']["targetMeanPrice"]['fmt']
    print(f"""
    These are our reccomendations based on the fundamental analysis: 
    --------------------------------------------------------------------
    
    {ticker}'s previous closing price was ${previous_price}. With a 52 week high of ${fifty_two_weekHigh}. 
    Expert analysis has it rated as a {buy_sell}. 

    Important metics:
    Cash flow (+/-): {cash_flow} 
    Debt to equity: {debt_to_equity}
    Return on equity(ROE): {returnOnEquity}
    Target price: ${targetMeanPrice}
    --------------------------------------------------------------------
     > """)
#-------------------------------------------------------API---------------------------------------------------------------#


#----------------------------------------------------user promps----------------------------------------------------------#


def promp():
    choice = input("""
    Enter one of the options below:
    --------------------------------------------------------------------
      1. News
      2. Analysis [...]
      3. Reccomendations
      4. Chart
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


def chart(ticker):
    start_date = input("START DATE: (M/D/YYYY) ")
    end_date = input('END DATE: (M/D/YYYY) ')

    stock_weekly = get_data(ticker, start_date=start_date,
                            end_date=end_date, index_as_date=True, interval="1wk")

    stock_weekly['MA9'] = stock_weekly.close.rolling(9).mean()
    stock_weekly['MA20'] = stock_weekly.close.rolling(20).mean()
    '''
    candlestick = go.Candlestick(
        x=stock_weekly.index,
        open=stock_weekly['open'],
        high=stock_weekly['high'],
        low=stock_weekly['low'],
        close=stock_weekly['close']
    )
    '''

    fig = go.Figure(data=[go.Candlestick(
        x=stock_weekly.index,
        open=stock_weekly['open'],
        high=stock_weekly['high'],
        low=stock_weekly['low'],
        close=stock_weekly['close']),
        go.Scatter(x=stock_weekly.index, y=stock_weekly.MA9,
                   line=dict(color='purple', width=1)),
        go.Scatter(x=stock_weekly.index, y=stock_weekly.MA20, line=dict(color='blue', width=1))])

    fig.update_layout(
        width=1200, height=700,
        title=f'{start_date} to {end_date}',
        yaxis_title=f"{ticker}'s Price action",
        xaxis_title="Date",
        xaxis_rangeslider_visible=False,
        template="plotly_dark"
    )

    print(fig.show())

#----------------------------------------------------user promps----------------------------------------------------------#


ticker = input("Input ticker symbol: ").upper()

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
        chart(ticker)

    elif choice == "5":
        break
    else:
        print(f'{choice} is not a option. ')
        break
