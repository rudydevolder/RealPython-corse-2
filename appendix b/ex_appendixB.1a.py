# ex_appendixB.1a.py - FTP Directory Listing


import ftplib

server = 'ftp.secureftp-test.com'
username = 'test'
password = 'test'

# Initialize and pass in FTP URL and login credentials (if applicable)
ftp = ftplib.FTP(host=server, user=username, passwd=password)

# Create a list to receive the data
data = []

# Appends the directories and files to the list
ftp.dir(data.append)

# Closes the connection
ftp.quit()

# Prints out the directories and files, line by line
for l in data:
   print(l)
