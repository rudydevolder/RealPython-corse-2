# ex2.6b.py - Create a table and populate it with data


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # create a table
    c.execute("""CREATE TABLE regions
              (city TEXT, region TEXT)
               """)

    # insert multiple records using a tuple
    # (again, copy and paste the values if you'd like)
    cities = [
            ('New York City', 'Northeast'),
            ('San Francisco', 'West'),
            ('Chicago', 'Midwest'),
            ('Houston', 'South'),
            ('Phoenix', 'West'),
            ('Boston', 'Northeast'),
            ('Los Angeles', 'West'),
            ('Houston', 'South'),
            ('Philadelphia', 'Northeast'),
            ('San Antonio', 'South'),
            ('San Diego', 'West'),
            ('Dallas', 'South'),
            ('San Jose', 'West'),
            ('Jacksonville', 'South'),
            ('Indianapolis', 'Midwest'),
            ('Austin', 'South'),
            ('Detroit', 'Midwest')
             ]

    # insert data into table
    c.executemany("INSERT INTO regions VALUES(?, ? )", cities)

    # retrieve data
    c.execute("SELECT * FROM regions ORDER BY region ASC")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]
