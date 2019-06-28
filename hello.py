import urllib.request

webUrl = urllib.request.urlopen('http://www.iltalehti.fi')
print(str(webUrl.getcode()))

#request needs to be installed