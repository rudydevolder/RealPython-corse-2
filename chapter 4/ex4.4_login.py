    # ex4.4_login.py - login


    #!/usr/bin/env python
    import cgi
    import Cookie

    # get post data
    form = cgi.FieldStorage()
    post_user = form.getfirst('user', '')
    post_password = form.getfirst('password', '')

    # define username and password
    username = "admin"
    password = "admin"

    if post_user == username and post_password == password:
        # if authentication is ok
        thiscookie = Cookie.SimpleCookie()
        thiscookie['logged_in'] = True
        print thiscookie
        print "Refresh: 0; url=ex4.4_blog5.py\r\n"
    else:
        # if authentication failed
        print "Refresh: 0; url=../ex4.4_login.html\r\n"

