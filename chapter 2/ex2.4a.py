# ex2.4a.py - SELECT statement


import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # use a for loop to iterate through the database, printing the results line by line
    for row in c.execute("select firstname, lastname from employees"):
        print row




