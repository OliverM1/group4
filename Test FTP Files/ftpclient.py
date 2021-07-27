from ftplib import FTP
import os

#where to download to
os.chdir("temp")


#connect to local hosted ftp server
ftp = FTP("127.0.0.1")
ftp.login()

#change to the folder where all the files are 
ftp.cwd("FTP")

#list all files
files = ftp.nlst()


#download each file
for file in files:
    #creates a local copy of the file
    with open(file,'wb') as local:
        #writes data from the remote to the local
        ftp.retrbinary('RETR ' + file, local.write)


ftp.close()