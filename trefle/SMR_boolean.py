import requests
from urllib.parse import urlencode
import urllib.parse as urlparse

boolean_vars = [
    'fruit_conspicuous',
    'coppice_potential',
    'resprout_ability',
    'propagated_by_sprigs',
    'propagated_by_cuttings',
    'fodder_product',
    'fire_resistance',
    'fall_conspicuous',
    'propagated_by_container',
    'flower_conspicuous',
    'adapted_to_medium_textured_soils',
    'veneer_product',
    'christmas_tree_product',
    'pulpwood_product',
    'small_grain',
    'low_growing_grass',
    'berry_nut_seed_product',
    'propagated_by_bare_root',
    'propagated_by_sod',
    'adapted_to_fine_textured_soils',
    'post_product',
    'propagated_by_seed',
    'nursery_stock_product',
    'cold_stratification_required',
    'fruit_seed_persistence',
    'propagated_by_bulbs',
    'leaf_retention',
    'known_allelopath',
    'palatable_human',
    'propagated_by_tubers',
    'lumber_product',
    'adapted_to_coarse_textured_soils',
    'propagated_by_corms',
    'naval_store_product'
]
fetched_items = []
for i in boolean_vars:
    api_base = 'https://trefle.io/api/species?token=d1FuZXdYOVpKczQvZzI0VERPTjZwdz09'
    params1 = {i: 'false'}
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
