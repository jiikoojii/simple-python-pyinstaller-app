import urllib.request
import urllib.parse
import re

url = 'https://www.ilmatieteenlaitos.fi'
values = {'s':'basics',
		'submit':'searh'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
print(paragraphs)