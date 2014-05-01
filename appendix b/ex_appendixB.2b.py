# ex_appendixB.2b.py - SFTP File Download


import pysftp
import sys

server = ''
username = ''
password = ''

# Defines the name of the file for download
file_name = sys.argv[1]

# Initialize and pass in SFTP URL and login credentials (if applicable)
sftp = pysftp.Connection(host=server, username=username, password=password)

# Download the file from the remote server
sftp.get(file_name)

# Closes the connection
sftp.close()
