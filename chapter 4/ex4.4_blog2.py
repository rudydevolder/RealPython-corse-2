# ex4.4_blog2.py - Query reviews tables, aggregate total of posts


# import the sqlite3 library
import sqlite3

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # total posts
    c.execute("SELECT COUNT(post) FROM posts")
    total = c.fetchone()[0]
    print "Total Posts: ", total

    # query posts
    c.execute("SELECT * FROM posts")

    # fetchall() retrieves all records from the query
    posts = c.fetchall()

    print "\nBlog Posts\n==========="

    # output the rows to the screen, row by row
    for p in posts:
        print "Title: ", p[0]
        print "Post: ", p[1], "\n"
