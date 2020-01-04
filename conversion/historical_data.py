import requests
import json
import datetime


def historical_data(Date, currency_symbol):

    api_key = "863c2a9a82c6e60e9d8451c59b0c3104"

    URL = ('http://api.coinlayer.com/api/%s?target=%s&access_key=%s' %
           (Date, currency_symbol, api_key))
    request = requests.get(URL)
    result = request['rate']
    target = result['target']
    i = 0
    for sym, value in enumerate(target):
        i += 1
        print('the value of ' + sym + 'on' + Date + 'is' + value)

        #select the top 5 result
        if i == 4:
            break
