# ex2.3c.py - import from CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # open the csv file and assign to a variable
    employees = csv.reader(open("employees.csv", "rU"))

    # create a new table called employees
    c.execute("create table employees(firstname, lastname)")

    # insert data into table
    c.executemany("insert into employees(firstname, lastname) values (?, ?)", employees)

