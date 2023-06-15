import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

pos = input('Enter position: ')
countx = input('Enter count: ')
p = int(pos)
countx = int(countx)

url = input('Enter - ')
countb = 0
while True :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    count = 0
    tags = soup('a')
    url = None
    for tag in tags:
        url = tag.get('href', None)
        count+=1
        if count>=p :
            print("Retrieving: ",url)
            break
    countb+=1
    if countb>=countx : break

"""
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
"""
