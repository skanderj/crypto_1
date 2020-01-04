
import requests
import json
import datetime



def curency_coversation(query, target, amount):

    #convert thet input to uper case
    Query = query.upper()
    api_key = '863c2a9a82c6e60e9d8451c59b0c3104'
    URL = ('''https://api.coinlayer.com/convert?access_key=%s
            &from=%s&to=%s&amount=%s''' % (api_key, Query, target, amount))

    request = requests.get(URL)
    currency = request['query']
    rate = request['info']['rate']
    result = request['result']
    conversation = ('''the value of %s %s  today is equale to %s and the rate is %s ''' % (
        currency, amount, result, rate))
    return conversation
