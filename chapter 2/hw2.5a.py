# hw2.5a.py - INSERT, UPDATE and SELECT statements

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # insert multiple records using a tuple
    cars = [
            ('Ford', 'Focus', 30000),
            ('Ford', 'Fusion', 1300),
            ('Ford', 'Taurus', 300),
            ('Honda', 'CR-Z', 700),
            ('Honda', 'Crosstour', 3000)
             ]

    # insert data into table
    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', cars)

    # update data
    c.execute("UPDATE inventory SET quantity = 7000 WHERE model='Crosstour'")
    c.execute("UPDATE inventory SET quantity = 100 WHERE model='Taurus'")

    # retrieve data
    c.execute("SELECT * FROM inventory")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2]

    print "\nFord:\n"

    # retrieve data
    c.execute("SELECT * FROM inventory WHERE make='Ford'")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1], r[2]
