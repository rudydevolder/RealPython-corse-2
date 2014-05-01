# ex4.4_blog1.py - Create a SQLite3 table and populate it with data


import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

	# get a cursor object used to execute SQL commands
	c = connection.cursor()

	# create the table
	c.execute("""CREATE TABLE posts(title TEXT, post TEXT)""")

	# insert multiple records using a tuple
	posts = [
	("Good", "I\'m good."),
	("Well", "I\'m well."),
	("Excellent", "I\'m excellent."),
	("Okay", "I\'m okay.")
	]

	# insert data into table
	c.executemany('INSERT INTO posts VALUES(?, ?)', posts)