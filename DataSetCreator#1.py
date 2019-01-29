import cv2
import os
from ctypes import *
import sqlite3

cam = cv2.VideoCapture(0) #Camera Function
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def MessageBox(title, text, style): #Definition of MessageBox
    sty = int(style) + 4096
    return windll.user32.MessageBoxA(0, text, title, sty) #MB_SYSTEMMODAL==4096

if os.path.isfile('EMPLOYEE_DB.db'):       #Check the existence of database
   conn = sqlite3.connect('EMPLOYEE_DB.db')  #Creating Database
                                          #Creation of table into database                           
   conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE_DETAILS     
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         GENDER         CHAR(50),
         DESIGNATION    TEXT    NOT NULL,
         SHIFT          CHAR(10),
         CONTACT_NO     INT);''')
else:
     conn = sqlite3.connect('EMPLOYEE_DB.db')  #Creating Database if doesn't exists
                                                                       
     conn.execute('''CREATE TABLE IF NOT EXISTS EMPLOYEE_DETAILS     
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         GENDER         CHAR(50),
         DESIGNATION    TEXT    NOT NULL,
         SHIFT          CHAR(10),
         CONTACT_NO     INT);''')
    

empid=raw_input('Enter Your ID: ')              #Taking User Inputs
name=raw_input('Enter Your Name: ')
gender=raw_input('Enter Your Gender: ')
designation=raw_input('Enter Your Designation: ')
shift=raw_input('Enter Your Shift(M,G,B,FN,N): ')
contactno=raw_input('Enter Your Contact NO: ')

conn = sqlite3.connect('EMPLOYEE_DB.db')        #Insertion of data into database
conn.execute("Insert into EMPLOYEE_DETAILS (ID, NAME, GENDER, DESIGNATION, SHIFT, CONTACT_NO) Values (?, ?, ?, ?, ?, ?)", (empid, name, gender, designation, shift, contactno))
conn.commit()


sampleNum=0                                 #Create the dataset of employees
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #Convert the colored image into gray
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                                     #incrementing sample number 
        sampleNum=sampleNum+1
                                     #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+empid +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        

        cv2.imshow('frame',img)
                                     #wait for 100 miliseconds 
    if cv2.waitKey(100)== ord('q'):
        break;
                                     # break if the sample number is morethan 80
    elif sampleNum>80:
        break;

cam.release()
conn.close()
MessageBox('FACE RECOGNITION', 'DATA STORED', 64) #Message of completion
cv2.destroyAllWindows()

