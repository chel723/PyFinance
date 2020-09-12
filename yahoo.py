import pandas as pd
import yfinance as yf

df_yahoo = yf.download('AAPL',
                       start ='2020-01-01',
                       end = '2020-07-01',
                       progress=False)

df_yahoo.to_csv('/Users/chelseaw/Desktop/yahooFinance.csv')

fileYahoo = open('/Users/chelseaw/Desktop/yahooFinance.csv')
print(fileYahoo.read())
