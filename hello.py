import urllib

link = "http://www.iltalehti.fi"
f = urllib.urlopen(link)
myfile = f.read()
print(myfile)