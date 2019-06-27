import urllib

link = "http://www.iltalehti.fi"
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)