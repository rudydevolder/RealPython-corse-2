# ex4.3g.py - cgitb module

#!/usr/bin/env python
import cgitb
cgitb.enable()
print "Content-Type: text/html"
print
print 1/0
