import requests

link = "http://www.iltalehti.fi"
f = requests.get(link)
print(f.text)