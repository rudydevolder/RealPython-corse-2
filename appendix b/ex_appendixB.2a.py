# ex_appendixB.2a.py - SFTP Directory Listing


import pysftp

server = ''
username = ''
password = ''

# Initialize and pass in SFTP URL and login credentials (if applicable)
sftp = pysftp.Connection(host=server, username=username, password=password)

# Get the directory and file listing
data = sftp.listdir()

# Closes the connection
sftp.close()

# Prints out the directories and files, line by line
for l in data:
   print(l)
