# SMR5: Correct postal code should give correct results and incorrect postal code should not give correct results.
# FAILURE CAUSING
# Postal_code: -18364 returns city Arlington Heights, Illinois which has postal codes: 60004, 60005, and 60006

import requests
import random
from urllib.parse import urlencode
import urllib.parse as urlparse

api_base = 'http://api.weatherbit.io/v2.0/current'
key = 'c08a23a088524ed88c152b52b7176051'
params = {'postal_code': -18364, 'key': key}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params)
url_parts[4] = urlencode(query)
api = urlparse.urlunparse(url_parts)
data1 = requests.get(api).json()