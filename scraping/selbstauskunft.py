import re
import csv


name = 'banken'
max_pages = 11

import requests

url = f'https://selbstauskunft.net/unternehmen/{name}/seite/'
url_item = 'https://selbstauskunft.net/unternehmen/'

headers = ['id', 'name', 'street', 'pcode', 'city', 'email', 'url', 'contact_url', 'phone', 'comment', 'state', 'created_at', 'updated_at',
           'mailing_mode', 'cached_tag_list', 'slug', 'approved_at', 'inquiry_kind', 'department', 'objection_kind', 'gv_numer', 'gv_number', 'tag_ids']

dicts = []

added = set()

for i in range(max_pages):
    r = requests.get(url + str(i))
    text = r.text
    for x in re.findall(r'<a href="/unternehmen/(\d+)', text):
        if x in added:
            continue
        added.add(x)
        r_item = requests.get(url_item + x + '.json')
        dicts.append(r_item.json()['company'])
        print(x)

with open(f'data/{name}.csv', 'w', newline='') as csvfile:
    fieldnames = headers
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(dicts)
