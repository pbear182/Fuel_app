from feedparser import parse
from pprint import pprint

from urllib.parse import urlencode

from itertools import product

from datetime import datetime
dateTimeObj = str(datetime.now())

def get_fuel(product_id, region, day):
  params = {
    'Product': product_id,
    'Region': region,
    'Day': day,
  }
  data = parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode(params))
  return [
      {
            'date': details['date'],
            'address': details['address'],
            'suburb': details['location'],
            'brand': details['brand'],
            'price': float(details['price']),
      }
      for details in data['entries']
  ]

NineEight_today = get_fuel(6, 26, 'Today')
NineEight_tmr = get_fuel(6, 26, 'Tomorrow')
Combined_NineEight = NineEight_today + NineEight_tmr

def by_price(item):
    return item['price']
sorted_Combined_NineEight = sorted(Combined_NineEight, key = by_price)

tr_list = [
    '<tr><td>{date}</td><td>{address}</td><td>{suburb}</td><td>{brand}</td><td>{price}</td></tr>'.format(**word)
    for word in  sorted_Combined_NineEight
]

tableheading = '''
    <h2>Fuel Table</h2>

    <tr>
        <th>Date</th>
        <th>Address</th>
        <th>Location</th>
        <th>Brand</th>
        <th>Price</th>
    </tr>
'''

html = '<table>' + tableheading + str({dateTimeObj}) + ''.join(tr_list) + '</table>'

with open('Fuel.html', 'w') as f:
        f.write('<style>table, td{border: 1px solid blue}</style>' + html)




