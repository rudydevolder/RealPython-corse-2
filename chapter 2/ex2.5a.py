# ex2.5a.py - UPDATE and DELETE statements

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE population SET population = 9000000 WHERE city='New York City'")

    # delete data
    c.execute("DELETE FROM population WHERE city='Boston'")

    print "\nNEW DATA:\n"

    # retrieve data
    c.execute("SELECT * FROM population")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2]
