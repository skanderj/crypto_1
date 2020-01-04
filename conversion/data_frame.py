import requests
import json
import datetime


def data_frame(start, end):

    apikey = '863c2a9a82c6e60e9d8451c59b0c3104'
    #set the input to string form

    start = str(input('enter strating date :'))
    #convert the input to right fotmat
    start_date = datetime.datetime.timestamp(start).strtime('% Y-%m-%d')
    #get the curret date
    end = '{d:%Y-%m-%d}'.format(d=datetime.datetime.now())
    #input exemple
    unit_1 = 'BTC'
    unit_2 = 'ERU'

    URL = ('''http://api.coinlayer.com/timeframe?access_key=%s&start_date=%s&end_date=%s&symbols=%s,%s'''
           % (apikey, start_date, end, unit_1, unit_2))

    response = requests.get(URL)
    result = response['rate']
    day_changes = []
    for date in result:
        change = result[date]
        #store the information in dictionary object
        data_frame = {'date': result[date],
                      unit_1: change[unit_1], unit_2: change[unit_2]}
        conversation_day = ('the rate at %s is : %s on BTC and %s on ERU') % (
            data_frame['data'], str(data_frame['BTC']), str(data_frame['ERU']))
        day_changes.append(data_frame)
        return conversation_day
    # to collect all days conversation in list
    #return day_changes


end = '{d:%Y-%m-%d}'.format(d=datetime.datetime.now())
data_frame(2019-12-28, end)
