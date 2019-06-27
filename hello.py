import requests

link = "http://www.iltalehti.fi"
f = requests.get(link)
print(f.text)

#request needs to be installed