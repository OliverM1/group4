from ftplib import FTP
import os
import re

class ftpclient:
    def __init__(self,*,regex_str,server_ip,port):
        self.server_ip = server_ip
        self.port = port
        self.regex = re.compile(regex_str)
        self.files = []

    def connect(self):
        #connect to local hosted ftp server
        self.__ftp = FTP()
        self.__ftp.connect(self.server_ip,self.port)
        self.__ftp.login()
        #change to the folder where all the files are 
        self.__ftp.cwd("FILES")

    def disconnect(self):
        self.__ftp.close()

    #run before download
    def match(self):
        #list all files
        files = self.__ftp.nlst()
        self.__files = list(filter(self.regex.match,files))
        return len(self.__files)

    def download(self):
        #where to download to
        os.chdir("temp")
        for file in self.__files:
                with open(file,'wb') as local:
                    #writes data from the remote to the local
                    self.__ftp.retrbinary('RETR ' + file, local.write)
        os.chdir("..") # change back




