# hw_appendixB.1a.py - FTP


import ftplib
import sys

server = ''
username = ''
password = ''

# Initialize and pass in FTP URL and login credentials (if applicable)
ftp = ftplib.FTP(host=server, user=username, passwd=password)


# 1. LIST DIRECTORY CONTENTS:
# Create a list to receive the data
data = []

# Appends the directories and files to the list
ftp.dir(data.append)

# Prints out the directories and files, line by line
for l in data:
   print(l)


# 2. CHANGE REMOTE DIRECTORY AND LIST CONTENTS:
# Change remote directory
ftp.cwd('htdocs')
print '\n\n changed to htdocs:\n'

# Reset the list that will receive the data
data = []

# Appends the directories and files to the list
ftp.dir(data.append)

# Prints out the directories and files, line by line
for l in data:
   print(l)


# 3. UPLOAD FILE:
# Defines the name of the file for upload
file_name = 'bookstore.xml'

# Opens the local file to upload
with open(file_name, "rb") as f:
    # Write the contents of the local file to the remote file
    ftp.storbinary("STOR " + file_name, f)


# 4. DOWNLOAD FILE:
# Defines the name of the file to download
file_name = 'index2.html'

# Create a local file with the same name as the remote file
with open(file_name, "wb") as f:
    # Write the contents of the remote file to the local file
    ftp.retrbinary("RETR " + file_name, f.write)


# Closes the connection
ftp.quit()
