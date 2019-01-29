import sqlite3
import cv2

conn1 = sqlite3.connect('TS_DATABASE.db')

print "Timestamp database opened successfully";
empid= raw_input("enter your required id:")

cursor = conn1.execute("SELECT TS_ID,NAME,DATE,TIME,D_YEAR,D_MONTH,D_DAY FROM TS_DATA3 WHERE TS_ID=?",(empid,))
#empid = cursor.fetchone()
#cursor = conn1.execute("SELECT * FROM TS_DATA3 LIMIT 1")

#date = 0



for row in cursor:
  
   
    print "TIMESTAMP_ID = ", row[0]
    print "Name = ",row[1]
    print "DATE = ", row[2]
    print "TIME = ", row[3]
    print "Y = ", row[4]
    print "M = ", row[5]
    print "D = ", row[6]
    m=row[5]

    
     
    
    
#cursor = conn1.execute("DELETE FROM TIMESTAMP_DATA")
#conn1.commit()
   

    
print "Operation done successfully";
conn1.close()
