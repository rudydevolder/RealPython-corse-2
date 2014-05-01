# ex4.4_blog4.py - Main Page


# import the libraries
import sqlite3
import cgi
import os

# set http header
print "Content-Type: text/html"
print

# get post data
form = cgi.FieldStorage()
title = form.getfirst('title', '')
post = form.getfirst('post', '')

# create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:

    # get a cursor object used to execute SQL commands
    c = connection.cursor()

    # insert data to db if not empty
    if title != "" and post != "":
        # insert data into table
        c.execute('INSERT INTO posts VALUES(?, ?)', (title, post))

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
        <div>
          <form method="POST" action="ex4.4_blog4.py">
            <h2>Add New Post:</h2>
            <p>Title: <input type="text" name="title" value=""></p>
            <p>Post: <input type="text" name="post" value=""></p>
            <input type="submit" value="Submit">
          </form>
         </div>
      </body>
    </html>
    """ % (total, data_table)
