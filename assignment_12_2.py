import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter ')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
i = 0
while i < count:

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')

    lst = list()

    for tag in tags:
        urls = tag.get('href')
        lst += (urls.split())
    url = lst[position]
    i += 1
    print(lst[position])




