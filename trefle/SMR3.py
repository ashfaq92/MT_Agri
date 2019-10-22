# SMR2: Test difference MROP on species using  filter
import requests
from urllib.parse import urlencode
import urllib.parse as urlparse

api_base = 'https://trefle.io/api/species?token=d1FuZXdYOVpKczQvZzI0VERPTjZwdz09'

params1 = {'propagated_by_seed': 'true'}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params1)
url_parts[4] = urlencode(query)
api1 = urlparse.urlunparse(url_parts)
resp1 = requests.get(api1)
fetched_items1 = resp1.headers._store.get('total')[1]

params2 = {'propagated_by_seed': 'false'}
url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(params2)
url_parts[4] = urlencode(query)
api2 = urlparse.urlunparse(url_parts)
resp2 = requests.get(api2)
fetched_items2 = resp2.headers._store.get('total')[1]


url_parts = list(urlparse.urlparse(api_base))
query = dict(urlparse.parse_qsl(url_parts[4]))
url_parts[4] = urlencode(query)
api3 = urlparse.urlunparse(url_parts)
resp3 = requests.get(api3)
fetched_items3 = resp2.headers._store.get('total')[1]
