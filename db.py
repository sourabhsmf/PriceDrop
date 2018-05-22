import sqlite3
import datetime

class products(utility):
    def __init__(self):
        
        self.price = 0
        self.name = ""
        self.url = ""
        self.query = ""
        if DBFILE_AVAILABILITY_FLAG:
            self.conn = sqlite3.connect("test.db")
            self.c = self.conn.cursor() 
    
    def add(self):
    
        self.query = "INSERT INTO PRODUCTS (name , price , url , timestamp) values (? , ? , ? , ?) "
        self.c.execute( self.query , (self.name , self.url , self.price , str(datetime.datetime.now())))
        self.conn.commit()
    
    def get(self, clause ,value):
        if clause in ["price" , "url" , "name"]:
            self.query = "SELECT * FROM PRODUCTS WHERE " + eval("self." + clause" + "= ?") 
            self.c.execute(self.query , value)
        return self.c.fetchall()
    def getAll():

        self.query = "SELECT * FROM PRODUCTS" 
        return self.c.fetchall()
        #print(c.fetchall())
    


    #c = conn.cursor()
    #c.execute("CREATE TABLE PRODUCTS (name , price , url , timestamp)")
    #conn.close()
