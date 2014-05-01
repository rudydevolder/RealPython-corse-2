# ex4.4_logout.py - login


#!/usr/bin/env python
import Cookie

# unset the Cookie
thiscookie = Cookie.SimpleCookie()
thiscookie['logged_in'] = ''
print thiscookie

# redirect to login page
print "Refresh: 0; url=../ex4.4_login.html\r\n"
