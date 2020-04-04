"""
author: Muhammad Yudha Galang Fardana
This is a program to fetch forex rates from exchangeratesapi.io
and convert it into a dataframe.
It doesnt need an API key so you can just use it by changing 
the configuration variables.
"""
import pandas as pd
import requests
import json

# configuration variables
# API_KEY = 'PDX19q5fnnvUWPihxH7P'
base_currency = 'USD' # default: EUR
exch_currency = 'IDR' # target currency
startdate = '2019-01-01' # Beginning date (exclusive)
enddate = '2019-06-01' # Ending date (also exclusive)
mode = 'history' # history (historical) | latest (remove startdate and enddate from url)
url = f'https://api.exchangeratesapi.io/{mode}?start_at={startdate}&end_at={enddate}&base={base_currency}&symbols={exch_currency}'

# request method and fetching process
response = requests.get(url)
response_json = response.json()

# convert to pandas dataframes
df = pd.DataFrame(response_json['rates']).transpose().reset_index()
df.columns = ['date', exch_currency+'close']
df = df.sort_values(by=['date'], ignore_index = True)
print(df)