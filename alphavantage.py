import requests

url = 'https://www.alphavantage.co/query'

params_currency = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'SGD',
    'to_currency': 'GBP',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

params_crypto = {
    'function': 'CRYPTO_INTRADAY',
    'symbol': 'ETH',
    'market': 'SGD',
    'interval': '60min',
    'datatype': 'csv',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

params_ema = {
    'function': 'EMA',
    'symbol': 'FB',
    'interval': 'daily',
    'time_period': '30',
    'series_type': 'close',
    'datatype': 'json',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

params_crypex = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'BTC',
    'to_currency': 'USD',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

# Task 1
currency = requests.get(url, params=params_currency)
exchange_rate = currency.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(f'The exchange rate from SGD to GBP is: {exchange_rate}')

currency = requests.get(url, params=params_crypex)
exchange_rate = currency.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(f'The exchange rate from BTC to USD is: {exchange_rate}')

# Task 2 and 3
def GenerateFile (para):
    
    response = requests.get(url,params= para)
    content = response.content

    filename = para['function']
    fileformat = para['datatype']

    file = open(f'{filename}.{fileformat}','wb')
    file.write(content)
    file.close()

    return

GenerateFile(params_crypto)
GenerateFile(params_ema)