# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_777995.html", context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
span_tag = soup("span")

suma = 0
count = 0
for tag in span_tag:
    suma = suma + int(tag.contents[0])
    count+= 1
print("Count: ",count)
print("Sum: ",suma)
