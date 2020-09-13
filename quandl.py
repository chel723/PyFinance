import pandas as pd
import quandl

QUANDL_KEY = '{key}'
quandl.Apiconfig.api_key = QUANDL_KEY

df_quandl= quandl.get(dataset = 'WIKI/AAPL',
                      start_date = '2000-01-01',
                      end_date = '2010-12-31')

df_quandl.to_csv('Users/chelseaw/Desktop/quandl')

fileQuandl = open('Users/chelseaw/Desktop/quandl')

print(fileQuandl.read())