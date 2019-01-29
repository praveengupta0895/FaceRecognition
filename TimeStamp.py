import sqlite3


         #Creating Database
#conn = sqlite3.connect('Timestamp.db')
#print "Opened database successfully";

         #Creation of table into database 1
"""conn = sqlite3.connect('Timestamp.db')
print "Opened database successfully";
conn.execute('''CREATE TABLE EMPLOYEES_DETAILS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         GENDER         CHAR(50),
         CONTACT_NO     REAL);''')
print "Table created successfully";
conn.close()"""

        #Creation of table into database 2
"""conn = sqlite3.connect('Timestamp.db')
print "Opened database successfully";
conn.execute('''CREATE TABLE TIMESTAMP_DETAILS
         (NAME           TEXT    NOT NULL,
          TIME_IN        INT     NOT NULL,
          TIME_OUT       INT     NOT NULL,
         TIMESTAMP_ID INT PRIMARY KEY     NOT NULL,
         FOREIGN KEY (TIMESTAMP_ID) REFERENCES EMPLOYEES_DETAILS(ID));''')
print "Table created successfully";
conn.close()"""

        #Insertion of records into database 1

"""conn = sqlite3.connect('Timestamp.db')
print "Opened database successfully";
conn.execute("INSERT INTO EMPLOYEES_DETAILS (ID, NAME, AGE, GENDER,CONTACT_NO) \
      VALUES (1, 'Praveen', 23, 'Male', 987654312 )");
conn.execute("INSERT INTO EMPLOYEES_DETAILS (ID, NAME, AGE, GENDER,CONTACT_NO) \
      VALUES (2, 'Nishtha', 22, 'Female', 123467788 )");
conn.commit()
print "Records created successfully";
conn.close()"""

       #Insertion of records into database 2

"""conn = sqlite3.connect('Timestamp.db')
print "Opened database successfully";
conn.execute("INSERT INTO TIMESTAMP_DETAILS (NAME, TIME_IN,TIME_OUT, TIMESTAMP_ID) \
      VALUES ('Praveen',0930,1030,1 )");
conn.execute("INSERT INTO TIMESTAMP_DETAILS (NAME, TIME_IN,TIME_OUT, TIMESTAMP_ID) \
      VALUES ('Nishtha',0730,1030,5 )");
conn.commit()
print "Records created successfully";
conn.close()"""


"""    #Showing records from database 
conn = sqlite3.connect('Timestamp.db')
print "Opened database successfully";
cursor = conn.execute("SELECT EMPLOYEES_DETAILS.NAME, TIMESTAMP_DETAILS.TIME_IN,TIMESTAMP_DETAILS.TIME_OUT from EMPLOYEES_DETAILS,TIMESTAMP_DETAILS WHERE EMPLOYEES_DETAILS.ID=TIMESTAMP_DETAILS.TIMESTAMP_ID ")
for row in cursor:
   print "NAME = ", row[0]
   print "TIME_IN = ", row[1]
   print "TIME_OUT = ", row[2],"\n"
print "Operation done successfully";
conn.close()"""







import datetime

        #Creation of table into database 3
"""conn = sqlite3.connect('Timestamp_Data.db')
print "Opened database successfully";
conn.execute('''CREATE TABLE TIMESTAMP_DATA
         (TIMESTAMP_ID    INT     NOT NULL,
          DATE            DATE    NOT NULL,
          TIME            TIME    NOT NULL);''')
print "Table created successfully";
conn.close()"""

      #Insertion of records into database 3

"""conn = sqlite3.connect('Timestamp_Data.db')
print "Opened database successfully";
now = datetime.datetime.now()
conn.execute("INSERT INTO TIMESTAMP_DATA (TIMESTAMP_ID,DATE, TIME )Values (?,?, ?)",(1,now.strftime("%Y-%m-%d "),now.strftime("%H:%M")))
conn.commit()
print "Records created successfully";
conn.close()"""


  #Showing records from database 
conn = sqlite3.connect('Timestamp_Data.db')
print "Opened database successfully";
cursor = conn.execute("SELECT TIMESTAMP_ID,DATE, TIME from TIMESTAMP_DATA")
for row in cursor:
   print "TIMESTAMP_ID  = ", row[0]
   print "DATE = ", row[1]
   print "TIME  = ", row[2],"\n"
print "Operation done successfully";
conn.close()
