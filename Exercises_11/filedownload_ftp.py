#FTP program for downloading a file
""""
FTP file downloader
Tested with Python >=3.6
By: JOR
 v0.1 20AUG20
"""
#importing ftplib and settings libraries
import ftplib
import settings.ftp as settings
# Make the connection
ftp = ftplib.FTP(settings.FTP['URL'])
# Anonymous login
ftp.login()
# Change to the correct directory
ftp.cwd(settings.FTP["PATH"])
# Retrieve the file
ftp.retrbinary("RETR " + settings.FTP["FILENAME"], open(settings.FTP["FILENAME"], 'wb').write)
#terminating the connection
ftp.quit()
