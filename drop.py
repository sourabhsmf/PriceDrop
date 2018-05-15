#TODO
#Create a sqlitedb file
#Test internet connectivity
#Add entry for urls and initialize with price
#Set ping interval(user choice)
#Set price drop matrix(user choice)
#Email or log high price drop or other mechanism

import requests as req
connection_flag = True
def checkConnection():
    global connection_flag
    try:
        req.get(url="https://www.google.com" , timeout=5)
    except (req.exceptions.Timeout, req.exceptions.ReadTimeout):
        connection_flag = False    
        print("No internet Connection")
    except:
        connection_flag = False
        print("Some issue encountered")
checkConnection()