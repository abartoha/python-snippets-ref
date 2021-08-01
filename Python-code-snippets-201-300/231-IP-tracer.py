"""Code snippets vol-47-snippet-231
   IP Tracer

Download all snippets so far:
https://wp.me/Pa5TU8-1yg

Blog: stevepython.wordpress.com

requirements:pip3 install requests

origin:
https://gist.github.com/angeloped/127395a702e66c563f70e992957218e3
"""
import webbrowser as wb
import requests

def _input(form):
    try:
        return raw_input(form)
    except:
        return input(form)


tracing = _input('Enter IP (defaults to your own IP if none): ')

req = requests.get('http://ip-api.com/json/{0}'.format(tracing)).json()

if req['status'] == 'success':
    result = '''
    IP:      {0}
    Address: {1}, {2} ({3})
    Region:  {4}
    Zip:     {5}
    T-zone:  {6}
    Coords:
        LAT:  {7}
        LON:  {8}
    ISP:     {9}
    Org:     {10}
    '''
    result = result.format(req['query'], req['city'], req['country'],
                           req['countryCode'], req['region'], req['zip'],
                           req['timezone'], req['lat'], req['lon'],
                           req['isp'], req['org'])

    print(result)

    mapping = '''[1] Google Map
[2] Ip Tracker
Which web service you'd like
to geolocate IP (select none to exit): '''

    choice = _input(mapping)

    if choice == '1':
        wb.open('https://www.google.com/maps/@{0},{1},13z'.
                                format(req['lat'], req['lon']))
    elif choice == '2':
        wb.open('https://www.ip-tracker.org/locator/ip-lookup.php?ip={0}'.
                                format(req['query']))
else:
    print('We FAILED attempting to track subject..')
