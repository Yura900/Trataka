from urllib2 import urlopen
html = urlopen("https://www.5gcamp.com/")

print(html.read())