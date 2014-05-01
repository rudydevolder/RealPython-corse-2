# ex4.3e.py - login


#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
# retrieve the user and password entered in the form; set to empty string if none
user = cgi.escape(form['user'].value) if 'user' in form else ''
passwd = cgi.escape(form['password'].value) if 'password' in form else ''
username = "admin"
password = "admin"
if user == username and passwd == password:
	msg = "Welcome {username}. You are now logged in.".format(username=username)
else:
	msg = "Incorrect username or password. Please try again."
print "Content-Type: text/html\n"
htmlFormat = """
<html>
<body>
<p>{msg}</p>
</body>
</html>
"""
print(htmlFormat.format(msg=msg))
