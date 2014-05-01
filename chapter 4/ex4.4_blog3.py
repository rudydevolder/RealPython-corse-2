# ex4.4_blog3.py - Query reviews tables, aggregate total of posts


# import the libraries
import sqlite3
import cgi
import os

# set http header
print "Content-Type: text/html"
print

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # total posts
    c.execute("SELECT COUNT(post) FROM posts")
    total = c.fetchone()[0]

    # query posts
    c.execute("SELECT * FROM posts")

    # fetchall() retrieves all records from the query
    posts = c.fetchall()

    data_table = "<table border=1><tr><th>Title</th><th>Post</th></tr>"
    for p in posts:
        data_table += "<tr>"
    	    data_table += "<td>%s</td>" % (p[0])
    	    data_table += "<td>%s</td>" % (p[1])
    	    data_table += "</tr>"
    data_table += "</table>"
    print """\
    <html>
      <head><title>Blog</title></head>
      <body>
        <h1><center>Bloggy</center></h1>
        <h2>Welcome!</h2>
        <p>Total Posts: %s</p>
        <p>%s</p>
      </body>
    </html>
    """ % (total, data_table)
