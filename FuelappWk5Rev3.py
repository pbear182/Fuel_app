from feedparser import parse
from pprint import pprint

from datetime import datetime
dateTimeObj = str(datetime.now())

def get_fuel(product_id,when):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Region=26&Day='+str(when)+''
    data = parse(url)

    fuel_list =[
            {
                'date': details['date'],
                'address': details['address'],
                'suburb': details['location'],
                'brand': details['brand'],
                'price': float(details['price']),
            }
            for details in data['entries']    
        ]
    pprint(fuel_list)
    return fuel_list

unleaded = 1
premium_unleaded = 2
Octane = 6

NineEight_today = get_fuel(Octane,'today')
NineEight_tmr = get_fuel(Octane,'tomorrow')

Combined_NineEight = NineEight_today + NineEight_tmr

def by_price(item):
	return item['price']
sorted_Combined_NineEight = sorted(Combined_NineEight, key = by_price)

Fuel_html_list = [

# Keyword Arguments in Functions
# ** Converts dictionary item into argument
# ** for dictionaries, * for lists
    
    '<tr><td>{date}</td><td>{address}</td><td>{suburb}</td><td>{brand}</td><td>{price}</td></tr>'.format(**word)
       
    for word in sorted_Combined_NineEight
]

Fuel_html = f'''
<html>
<head>
<style>

</style>
</head>
<body>

<h2>Fuel Table</h2>

<p> {dateTimeObj} </p>

<table>
  <tr>
    <th>Date</th>
    <th>Address</th>
    <th>Location</th>
    <th>Brand</th>
    <th>Price</th>
  </tr>

<tr>
    {Fuel_html_list}
</tr>

</table>

</body>
</html>

'''
f = open('render.html', 'w')
f.write(Fuel_html)
f.close()


