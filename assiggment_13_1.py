import urllib.request, urllib.parse, urllib.error
import json


address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
comments = info["comments"]
print('User count:', len(comments))

sum = 0
for item in comments:
    sum += item['count']
print(sum)



# sample address: http://py4e-data.dr-chuck.net/comments_42.json