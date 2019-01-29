import sqlite3
import datetime
now = datetime.datetime.now()
conn = sqlite3.connect('TS_DATABASE.db')
cursor = conn.execute("SELECT * FROM TS_DATA ")
for row in cursor:
   #  print "ID: ",row[0]   ID
   #  print "NAME: ",row[1]  NAME
   #  print "DATE: ",row[2]  DATE
    #print "TIME: ",row[4]  

   
      
conn.close
