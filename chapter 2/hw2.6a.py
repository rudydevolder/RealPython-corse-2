# hw2.6a.py - SELECTing data from multiple tables

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a new table called orders
    c.execute("create table orders(make, model, order_date)")

    # insert multiple records using a tuple
    orders = [
            ('Ford', 'Focus', '2013-01-01'),
            ('Ford', 'Fusion', '2013-01-02'),
            ('Ford', 'Taurus', '2013-01-03'),
            ('Honda', 'CR-Z', '2013-01-04'),
            ('Honda', 'Crosstour', '2013-01-05'),
            ('Ford', 'Focus', '2013-01-06'),
            ('Ford', 'Fusion', '2013-01-07'),
            ('Ford', 'Taurus', '2013-01-08'),
            ('Honda', 'CR-Z', '2013-01-09'),
            ('Honda', 'Crosstour', '2013-01-10'),
            ('Ford', 'Focus', '2013-01-11'),
            ('Ford', 'Fusion', '2013-01-12'),
            ('Ford', 'Taurus', '2013-01-13'),
            ('Honda', 'CR-Z', '2013-01-14'),
            ('Honda', 'Crosstour', '2013-01-15')
             ]

    # insert data into table
    c.executemany('INSERT INTO orders VALUES(?, ?, ?)', orders)

    # retrieve data
    c.execute("SELECT * FROM inventory")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        # output the car make, model and quantity to screen
        print r[0], r[1], "\n", r[2]

        # retrieve order_date for the current car make and model
        c.execute("SELECT order_date FROM orders WHERE make=? and model=?",
                (r[0], r[1]))

        # fetchall() retrieves all records from the query
        order_dates = c.fetchall()

        # output each order_date to the screen
        for order_date in order_dates:
            print order_date[0]
