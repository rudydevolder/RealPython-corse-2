# ex3.2a.py - Retrieveing a web page


import requests

# retrieve the web page
r = requests.get("http://www.python.org/")

print r.content
