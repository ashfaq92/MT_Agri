# FAILURE CAUSING
# SMR1: Default Parameters (lang = en) should have no affect on result
import requests
from urllib.parse import urlencode
import urllib.parse as urlparse

api_base = 'http://api.weatherbit.io/v2.0/current'
city = 'city=Raleigh,NC'
key = 'c08a23a088524ed88c152b52b7176051'
params = {'city': city, 'key': key}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
api = urlparse.urlunparse(url_parts)
data1 = requests.get(api).json()
data1_core = data1['data'][0]


params2 = {'lang': 'en', 'city': city, 'key': key}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params2)
url_parts[4] = urlencode(query)
api2 = urlparse.urlunparse(url_parts)
data2 = requests.get(api2).json()
data2_core = data2['data'][0]
if data1_core != data2_core:
    print('data not equal')
    data1_set = set(data1_core)

