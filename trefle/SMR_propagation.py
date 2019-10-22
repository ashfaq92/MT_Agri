import requests
from urllib.parse import urlencode
import urllib.parse as urlparse

boolean_vars = [
    'propagated_by_sprigs',
    'propagated_by_cuttings',
    'propagated_by_container',
    'propagated_by_bare_root',
    'propagated_by_sod',
    'propagated_by_seed',
    'propagated_by_bulbs',
    'propagated_by_tubers',
    'propagated_by_corms',
]
fetched_items = []
for i in boolean_vars:
    api_base = 'https://trefle.io/api/species?token=d1FuZXdYOVpKczQvZzI0VERPTjZwdz09'
    params1 = {i: 'true'}
    url_parts = list(urlparse.urlparse(api_base))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params1)
    url_parts[4] = urlencode(query)
    api1 = urlparse.urlunparse(url_parts)
    resp1 = requests.get(api1)
    print('items fetched:', format(resp1.headers._store.get('total')[1]))
    fetched_items.append(resp1.headers._store.get('total')[1])


total = 0
for i in fetched_items:
    total = total + int(i)
print(total)