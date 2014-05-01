# hw2.4a.py - SELECT statement, remove unicode characters

import csv
import sqlite3

with sqlite3.connect(":memory:") as connection:
    c = connection.cursor()

    # open the csv file and assign to a variable
    employees = csv.reader(open("employees.csv"))

    # create a new table called employees
    c.execute("create table employees(firstname, lastname)")

    # insert data into table
    c.executemany("insert into employees(firstname, lastname) values (?, ?)", employees)

    # use a for loop to iterate through the database, printing the results line by line
    for row in c.execute("select firstname, lastname from employees"):
        print row, "\n", row[0], row[1], "\n"

# close the database connection
connection.close()
