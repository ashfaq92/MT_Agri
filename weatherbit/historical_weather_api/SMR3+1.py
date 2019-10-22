# FAILURE CAUSING
# SMR3: Default Parameters (units = M) should have no affect on result
import requests
import json
import myfunc
from urllib.parse import urlencode
import urllib.parse as urlparse

api_base = 'http://api.weatherbit.io/v2.0/current'
key = 'c08a23a088524ed88c152b52b7176051'
resp = 'response equal'
while True:
    city = myfunc.get_city('cities.csv')
    params = {'city': city, 'key': key}
    url_parts = list(urlparse.urlparse(api_base))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    api = urlparse.urlunparse(url_parts)

    params2 = {'lan': 'en', 'units': 'M', 'city': city, 'key': key}
    url_parts = list(urlparse.urlparse(api_base))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params2)
    url_parts[4] = urlencode(query)
    api2 = urlparse.urlunparse(url_parts)

    data1 = requests.get(api).json()
    data2 = requests.get(api2).json()

    data1_c = json.dumps(data1['data'][0])
    data2_c = json.dumps(data2['data'][0])

    if myfunc.ordered(data1) == myfunc.ordered(data2):
        resp = 'response equal rerun'
        print(resp)
        continue
    elif data1['data'][0]['last_ob_time'] != data2['data'][0]['last_ob_time'] or data1['data'][0]['ob_time'] != \
            data2['data'][0]['ob_time']:
        print('rerun due to ob time')
        continue
    elif data1['data'][0]['ts'] != data2['data'][0]['ts']:
        print('rerun due to ts')
        continue
    elif data1['data'][0]['aqi'] != data2['data'][0]['aqi']:
        print('data different due to aqi')
        print('data1 aqi', format(data1['data'][0]['aqi']))
        print('data2 aqi', format(data2['data'][0]['aqi']))
        break
    else:
        resp = 'data different'
        print(resp)
        break
