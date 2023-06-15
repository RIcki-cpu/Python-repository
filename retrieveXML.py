import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving: ",url)

input = urllib.request.urlopen(url, context=ctx).read()
print("Retrieved ",len(input)," characters")
tree = ET.fromstring(input).find('comments')

counts = tree.findall('comment')
print('Count:', len(counts))

sumt = 0

for item in counts:
    sumt+=int(item.find('count').text)
print("Sum: ",sumt)
