import urllib.request
import urllib.parse

url = 'http://www.ilmatieteenlaitos.fi'
resp = urllib.request.urlopen(url)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
print(paragraphs)