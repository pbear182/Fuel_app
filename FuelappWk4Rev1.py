from feedparser import parse
from pprint import pprint

from datetime import datetime
dateTimeObj = str(datetime.now())

def get_fuel(product_id,when):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Region=26&Day='+str(when)+''
    data = parse(url)
    return data['entries']

unleaded = 1
premium_unleaded = 2
Octane = 6

recent = 'yesterday'
current = 'today'
future = 'tomorrow'

NineEight_today = get_fuel(Octane,current)
NineEight_tmr = get_fuel(Octane,future)

Combined_NineEight = NineEight_today + NineEight_tmr

def by_price(item):
	return item['price']
sorted_Combined_NineEight = sorted(Combined_NineEight, key = by_price)

Fuel_html_list = ''
for word in sorted_Combined_NineEight:
    #my_list += '<li>' + word + '</li>'
    #my_list += '<li>{}</li>'.format(word)
    Fuel_html_list = Fuel_html_list + '<td>' + word['date'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['address'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['location'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['brand'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['price'] + '</td>'
    Fuel_html_list = Fuel_html_list + '</tr>'

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


