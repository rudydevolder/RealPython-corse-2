#ex2.6d.py - JOINing data from multiple tables - cleanup


import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # retrieve data
    c.execute("""SELECT DISTINCT population.city, population.population,
                regions.region FROM population, regions WHERE
                population.city = regions.city ORDER by population.city ASC""")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print
