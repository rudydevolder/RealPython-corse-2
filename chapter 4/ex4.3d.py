# ex4.3d.py - cgi square root


#!/usr/bin/env python
import cgi, math
form = cgi.FieldStorage()
# retrieve the number entered in the form; set to 0 if none
value = cgi.escape(form['sqrt'].value) if 'sqrt' in form else 0
sqrt = str(math.sqrt(float(value)))
print "Content-Type: text/html\n"
htmlFormat = """
<html>
<body>
<p>Hi. The square root of {value} equals {sqrt}</p>
</body>
</html>
"""
print(htmlFormat.format(value=value, sqrt=sqrt))