import sqlite3
import datetime
def init():
    #Check for db file
    try:
        open("test.db").close()
    except FileNotFoundError:
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        c.execute("CREATE TABLE PRODUCTS (name , price , url , timestamp)")
        conn.close()
def putProducts(name , price, url):
    init()
    conn = sqlite3.connect("test.db")
    c = conn.cursor()    
    c.execute("INSERT INTO PRODUCTS (name , price , url , timestamp) values (? , ? , ? , ?)" , (name , url , price , str(datetime.datetime.now())))
    conn.commit()
    conn.close()
putProducts('A' , 'B' , 'C') 
def getAllProducts():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()    
    c.execute("SELECT * FROM PRODUCTS")
    print(c.fetchall())
getAllProducts()