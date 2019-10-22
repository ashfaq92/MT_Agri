# MR3: subset relation based on brandOwner

import json
import random
from urllib.request import urlopen, Request

for i in range(10):

    v_brands = ["Blair's Sauces and Snacks", "Warrnambool Cheese and Butter", "The Grand Sweets and Snacks",
                "Enrique Cassinelli and Sons", "San Miguel Food and Beverage", "S. M. Jaleel and Company"]

    data = {
        "brandOwner": "Nestle"
    }
    data_str = json.dumps(data).encode("utf-8")
    url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
    req = Request(url, data_str, {'Content-Type': 'application/json'})
    f = urlopen(req)
    for x in f:
        resp1 = json.loads(x)
    f.close()

    data = {
        "brandOwner": "Nestle, " + random.choice(v_brands) + ", " + random.choice(v_brands) + ", " + random.choice(
            v_brands)
    }
    data_str = json.dumps(data).encode("utf-8")
    url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
    req = Request(url, data_str, {'Content-Type': 'application/json'})
    f = urlopen(req)
    for x in f:
        resp2 = json.loads(x)
    f.close()

    if resp1['totalHits'] < resp2['totalHits']:
        print('good, rerun!', format(i))
        continue
    else:
        print('bad')
        break
else:
    print('unable to find fault')
