# ex_appendixB.1b.py - FTP File Download


import ftplib
import sys

server = 'ftp.secureftp-test.com'
username = 'test'
password = 'test'

# Defines the name of the file for download
file_name = sys.argv[1]

# Initialize and pass in FTP URL and login credentials (if applicable)
ftp = ftplib.FTP(host=server, user=username, passwd=password)

# Create a local file with the same name as the remote file
with open(file_name, "wb") as f:
    # Write the contents of the remote file to the local file
    ftp.retrbinary("RETR " + file_name, f.write)

# Closes the connection
ftp.quit()
