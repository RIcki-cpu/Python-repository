import json
import ssl
import urllib.request, urllib.parse, urllib.error


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location: ")
jsonfile = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved ', len(jsonfile), " characters")


info = json.loads(jsonfile)

suma = 0
count = 0
for element in info["comments"] :
    suma= suma + int(element["count"])
    count+=1
print("Count: ",count)
print("Sum: ",suma)
