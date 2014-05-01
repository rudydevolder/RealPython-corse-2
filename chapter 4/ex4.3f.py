# ex4.3f.py - cgi database access


#!/usr/bin/env python
import sqlite3
import cgi

print "Content-Type: text/xml"
print

with sqlite3.connect("names.db") as connection:
    c = connection.cursor()

    c.executescript("drop table if exists names")
    c.execute("create table names(first TEXT, last TEXT)")

    # insert multiple records using a tuple
    names = [
            ('John', 'Bell'),
            ('Michael', 'Sloane'),
            ('Rachel', 'Peterson')
             ]

    # insert data into table
    c.executemany('INSERT INTO names VALUES(?, ?)', names)

    c.execute("select first, last from names")

    # retrieve data
    rows = c.fetchall()

    # build xml string
    print "<names>"
    for r in rows:
    print "\t<name>"
    print "\t\t<first>%s</first>" % (r[0])
    print "\t\t<last>%s</last>" % (r[1])
    print "\t</name>"
    print "</names>"
