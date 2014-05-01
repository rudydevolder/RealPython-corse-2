# ex4.3c.py - cgi form handling


#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
# retrieve the name entered in the form; set to empty string if none
name = cgi.escape(form['name'].value) if 'name' in form else ''
print "Content-Type: text/html\n"
htmlFormat = """
<html>
<body>
<p>Hi, {name}</p>
</body>
</html>
"""
print(htmlFormat.format(name=name))