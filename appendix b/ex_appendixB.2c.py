# ex_appendixB.2c.py - SFTP File Upload


import pysftp
import sys

server = ''
username = ''
password = ''

# Defines the name of the file for upload
file_name = sys.argv[1]

# Initialize and pass in SFTP URL and login credentials (if applicable)
sftp = pysftp.Connection(host=server, username=username, password=password)

# Upload the file to the remote server
sftp.put(file_name)

# Closes the connection
sftp.close()
