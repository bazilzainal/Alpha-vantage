import requests
import time
from datetime import datetime

url = 'https://www.alphavantage.co/query'

sgd_to_gbp = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'SGD',
    'to_currency': 'GBP',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

btc_to_usd = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'BTC',
    'to_currency': 'USD',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

file_eth_intraday = {
    'function': 'CRYPTO_INTRADAY',
    'symbol': 'ETH',
    'market': 'SGD',
    'interval': '60min',
    'datatype': 'csv',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

file_fb_ema = {
    'function': 'EMA',
    'symbol': 'FB',
    'interval': 'daily',
    'time_period': '30',
    'series_type': 'close',
    'datatype': 'json',
    'apikey': 'C5DHIEK34Q4PVXGJ'
}

high_price = [0]

print(datetime.now().strftime('%H,%M,%S,%d,%m,%Y'))

# Task 1
def GetCurrency(paraminput):
    currency = requests.get(url, params=paraminput)
    exchange_rate = currency.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']
    from_currency = paraminput['from_currency']
    to_currency = paraminput['to_currency']
    current_time = datetime.now().strftime('%H,%M,%S,%d,%m,%Y')
    print(f'The exchange rate from {from_currency} to {to_currency} is: {exchange_rate}')

    f = open('btc_usd.csv', 'a')
    f.write(f'{current_time},{exchange_rate}\n')
    f.close()

    return [from_currency,to_currency,exchange_rate]


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


def CheckHighPrice(price):
    
    if float(price) > high_price[0]:
        high_price.append(float(price))
        high_price.pop(0)
        print('High price updated')
        print(f'High BTC-USD price is now {high_price[0]}')
        return float(price)


    return




while True:
    
    x = GetCurrency(btc_to_usd)
    CheckHighPrice(x[2])
    time.sleep(12)
    