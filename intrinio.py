import intrinio_sdk
import pandas as pd

intrinio_sdk.ApiClient().configuration.api_key['api_key'] = '{OjBkNDgwZTRhODgwMzgzNzU0OWI1NTM0YTA4NGNhYjI1}'
security_api = intrinio_sdk.SecurityApi()

r = security_api.get_security_stock_prices(identifier='AAPL',
                                           start_date = '2000-01-01',
                                           end_date = '2010-12-31',
                                           frequency = 'daily',
                                           page_size = 10000)

response_list = [x.to_dict() for x in r.stock_prices]
df_intrinio = pd.DataFrame(response_list).sort_values('date')
df_intrinio.set_index('date',inplace=True)

df_intrinio.to_csv('/Users/chelseaw/Desktop/intrinio.csv')

fileIntrinio = open('/Users/chelseaw/Desktop/intrinio.csv')

print(fileIntrinio.read())


