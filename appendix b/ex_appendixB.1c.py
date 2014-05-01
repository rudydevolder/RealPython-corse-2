# ex_appendixB.1c.py - FTP File Upload


import ftplib
import sys

server = ''
username = ''
password = ''

# Defines the name of the file for upload
file_name = sys.argv[1]

# Initialize and pass in FTP URL and login credentials (if applicable)
ftp = ftplib.FTP(host=server, user=username, passwd=password)

# Opens the local file to upload
with open(file_name, "rb") as f:
    # Write the contents of the local file to the remote file
    ftp.storbinary("STOR " + file_name, f)

# Closes the connection
ftp.quit()
