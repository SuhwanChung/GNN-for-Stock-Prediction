'''
Requires to create a list of ticker
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies
'''

import pandas as pd
#import yfinance as yf
from yahoofinancials import YahooFinancials

ticker = ['AAPL','TSLA', 'MSFT', 'FB']
yahoo_financials = YahooFinancials(ticker)

## 5 years
data = yahoo_financials.get_historical_price_data(start_date='2016-09-30',
                                                  end_date='2021-09-30',
                                                  time_interval='daily')

prices_df = pd.DataFrame({
    a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in ticker
})
