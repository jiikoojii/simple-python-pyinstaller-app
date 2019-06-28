import urllib.request

with urllib.request.urlopen('http://www.ilmatieteenlaitos.fi') as f:
	print(f.read(300))

#request needs to be installed