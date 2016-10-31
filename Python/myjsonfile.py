import json
import urllib
url = raw_input('Enter location: ')
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
#print 'Retrieved', len(data), 'characters'

decoded = json.loads(data)
#print 'User count:', len(info)
print '============================'
#print type(decoded)
print decoded
for item in decoded:
    print 'Name', decoded['name']
    print 'Count', decoded['count']