import sqlite3
conn = sqlite3.connect('FaceDB.db')
print "Opened database successfully";

cursor = conn.execute("SELECT * from EMPLOYEES")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "AGE = ", row[2]
   print "GENDER = ", row[3]
   print "CONTACT_NO = ", row[4], "\n"

print "Operation done successfully";
conn.close()
