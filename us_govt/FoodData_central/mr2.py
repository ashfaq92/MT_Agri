# Failure Causing
# M2: subset relations
"""
import json
import random
from urllib.request import urlopen, Request

input1 = "WHEAT"
input2 = "BREAD"
input3 = "WHEAT BREAD"
input4 = "WHEAT, BREAD"
# input5 = "WHEAT, BREAD, WHEAT BREAD, WHEAT BREAD, WHEAT VANILLA, CHOCOLATE && STRAWBERRY"
input5 = "WHEAT, BREAD, WHEAT BREAD, WHEAT BREAD, WHEAT VANILLA, CHOCOLATE AND STRAWBERRY"
data = {
    "generalSearchInput": input1,
    "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
    "sortDirection": random.choice(["asc", "desc"])
}
data_str = json.dumps(data).encode("utf-8")
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
req = Request(url, data_str, {'Content-Type': 'application/json'})
f = urlopen(req)
for x in f:
    resp1 = json.loads(x)
f.close()

######################################
data = {
    "generalSearchInput": input2,
    "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
    "sortDirection": random.choice(["asc", "desc"])
}
data_str = json.dumps(data).encode("utf-8")
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
req = Request(url, data_str, {'Content-Type': 'application/json'})
f = urlopen(req)
for x in f:
    resp2 = json.loads(x)
f.close()
######################################
data = {
    "generalSearchInput": input3,
    "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
    "sortDirection": random.choice(["asc", "desc"])
}
data_str = json.dumps(data).encode("utf-8")
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
req = Request(url, data_str, {'Content-Type': 'application/json'})
f = urlopen(req)
for x in f:
    resp3 = json.loads(x)
f.close()
######################################
data = {
    "generalSearchInput": input4,
    "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
    "sortDirection": random.choice(["asc", "desc"])
}
data_str = json.dumps(data).encode("utf-8")
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
req = Request(url, data_str, {'Content-Type': 'application/json'})
f = urlopen(req)
for x in f:
    resp4 = json.loads(x)
f.close()
######################################
data = {
    "generalSearchInput": input5,
    "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
    "sortDirection": random.choice(["asc", "desc"])
}
data_str = json.dumps(data).encode("utf-8")
url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
req = Request(url, data_str, {'Content-Type': 'application/json'})
f = urlopen(req)
for x in f:
    resp5 = json.loads(x)
f.close()
######################################
if resp5['totalHits'] > (resp1['totalHits'] or resp2['totalHits'] or resp3['totalHits'] or resp4['totalHits']):
    print('good')
else:
    print('bad')

"""

import json
import random
from urllib.request import urlopen, Request

food_terms = ['CHEWY TROPICAL POPPABLES CANDY, TROPICAL POPPABLES', 'PORK TAMALES IN RED SAUCE',
              'LIGHTLY SALTED BAKED GREEN PEA & CHICKPEA PUFFS, LIGHTLY SALTED',
              'ICE CREAM SANDWICHES ARTIFICIALLY FLAVORED VANILLA ICE CREAM WITH CHOCOLATE WAFERS, VANILLA',
              'VANILLA, CHOCOLATE AND STRAWBERRY ICE CREAM WITH CHOCOLATE WAFERS NEAPOLITAN SANDWICHES, VANILLA, CHOCOLATE AND STRAWBERRY',
              'PINK LADY BASIL ORGANIC KOMBUCHA, PINK LADY BASIL',
              'ARTIFICIALLY FLAVORED VANILLA ICE CREAM WITH CHOCOLATE WAFERS ICE CREAM SANDWICHES, VANILLA, CHOCOLATE WAFERS',
              'STRAWBERRY WAFERS BAKED WITH REAL STRAWBERRIES, STRAWBERRY', 'SEEDED JEWISH RYE BREAD, JEWISH RYE',
              'SWISS GOODIE RAISINS, ROASTED PEANUTS, MILK CHOCOLATE POKIES & ROASTED ALMONDS TRAIL MIX, SWISS GOODIE',
              'PRETZEL THINS', 'ROASTED & SALTED CASHEWS SPLITS & PIECES, ROASTED & SALTED',
              'ROASTED & SALTED SHELLED SUNFLOWER SEEDS, ROASTED & SALTED', 'PRETZEL STICKS', 'WHEAT BREAD, WHEAT',
              'ENRICHED MACARONI PRODUCT, ELBOW MACARONI', 'WHOLE ROASTED & SALTED CASHE']

for i in range(10):
    input1 = random.choice(food_terms)
    input2 = random.choice(food_terms)
    data = {
        "generalSearchInput": input1,
        "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
        "sortDirection": random.choice(["asc", "desc"])
    }
    data_str = json.dumps(data).encode("utf-8")
    url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
    req = Request(url, data_str, {'Content-Type': 'application/json'})
    f = urlopen(req)
    for x in f:
        resp1 = json.loads(x)
    f.close()

    data = {
        "generalSearchInput": input1 + ' ' + input2,
        "sortField": random.choice(["lowercaseDescription.keyword", "dataType.keyword", "publishedDate", "fdcId"]),
        "sortDirection": random.choice(["asc", "desc"])
    }
    data_str = json.dumps(data).encode("utf-8")
    url = 'https://api.nal.usda.gov/fdc/v1/search?api_key=HgevTUI0JDgzi7Y9XcHR3a3o9SQP6LfblaH4tnMZ'
    req = Request(url, data_str, {'Content-Type': 'application/json'})
    f = urlopen(req)
    for x in f:
        resp2 = json.loads(x)
    f.close()

    if resp1['totalHits'] > resp2['totalHits']:
        print('fault found')
        break
    elif resp1['totalPages'] > resp2['totalPages']:
        print('fault found')
        break
    elif resp1['totalHits'] / 50 > resp1['totalPages']:
        print('fault found')
        break
    elif resp2['totalHits'] / 50 > resp2['totalPages']:
        print('fault found')
        break
    else:
        print('response equal rerun ', format(i))
        continue

else:
    print('unable to find fault')
