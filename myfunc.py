import random


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def get_city(file):
    import csv
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = [row for row in csv_reader]
        city = random.choice(data)[0]
        return city


def remove_key(d, key):
    if key in d:
        del d[key]
    return d
