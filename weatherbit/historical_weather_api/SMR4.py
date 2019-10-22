# SMR4: Test latitude Longitude
# Latitudes range from -90 to 90.
# Longitudes range from -180 to 180.
# When lat or lon given out of range it should fail gracefully
# FAILURE CAUSING at lat = -15832 lon = -337.95 gives weather data of McMurdo Station Antarctica

import requests
import random
from urllib.parse import urlencode
import urllib.parse as urlparse

api_base = 'http://api.weatherbit.io/v2.0/current'
key = 'c08a23a088524ed88c152b52b7176051'
params = {'lat': random.uniform(-100000, -91), 'lon': random.uniform(-10000, -180), 'units': 'S', 'key': key}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
api = urlparse.urlunparse(url_parts)
data1 = requests.get(api).json()

if data1 == {'error': 'Invalid Parameters supplied.'}:
    print('OK')
else:
    print('bug found')
