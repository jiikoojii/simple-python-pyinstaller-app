import urllib.request

with urllib.request.urlopen('http://www.ilmatieteenlaitos.fi') as f:
	print(f.content())

#request needs to be installed