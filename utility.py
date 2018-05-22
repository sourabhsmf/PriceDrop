import requests

class utility():

    def __init__(self):
        #Specifies the internet connection 
        self.CONNECTION_FLAG = False
        #Specifies the availability of sqlite3 db file
        self.DBFILE_AVAILABILITY_FLAG = False
        #Specifies the availability of useragent file
        self.UAFILE_AVAILABILITY_FLAG = False
        #UserAgent for a request
        self.UserAgent = ""
    
    def initConnection(self):
        try:
            requests.get(url="https://www.google.com" , timeout=5)
        except (requests.exceptions.Timeout, req.exceptions.ReadTimeout):
            print("No internet Connection")
        except:
            print("Some issue encountered")
        self.CONNECTION_FLAG = True

    def initDBFile(self):
        #Check for db file
        try:
            open("test.db").close()
        except FileNotFoundError:
            #Create DB file
            open("test.db" , "w+").close()
        self.DBFILE_AVAILABILITY_FLAG = True

    def initUAFile(self):
        try:
            open("useragents.txt").close()
        except FileNotFoundError:
            open("useragents.txt" , "w+").close()
        self.UAFILE_AVAILABILITY_FLAG = True
