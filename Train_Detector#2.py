import cv2,os
import cv2
import numpy as np
from PIL import Image
from ctypes import *
import sqlite3
import datetime


recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def MessageBox(title, text, style):  #Message box defination
    sty = int(style) + 4096
    return windll.user32.MessageBoxA(0, text, title, sty) #MB_SYSTEMMODAL==4096

conn = sqlite3.connect('EMPLOYEE_DB.db') #Opening Employee Database
conn1 = sqlite3.connect('TS_DATABASE.db') #Opening TS_DATABASE Database
                                            #Creating table TS_DATA in TS_DATABASE
conn1.execute('''CREATE TABLE IF NOT EXISTS TS_DATA3
         (TS_ID    INT     NOT NULL,
          NAME            STRING  NOT NULL,
          DATE            DATE    NOT NULL,
          TIME            TIME    NOT NULL,
          D_YEAR          INT,
          D_MONTH         INT,
          D_DAY           INT);''')
#print "database created"

def getImagesWithID(path):
                                            #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
                                            #create empth face list
    faceSamples=[]
                                            #create empty ID list
    Ids=[]
                                            #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:

                                            # Updates in Code
                                            # ignore if the file does not have jpg extension :
        if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
            continue

                                            #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
                                             #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
                                             #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
                                             # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
                                             #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


faces,Ids = getImagesWithID('dataSet')
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainer.yml') 
cv2.destroyAllWindows()


recognizer.read('recognizer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
cursor = conn.execute("SELECT ID, NAME, GENDER, DESIGNATION, SHIFT, CONTACT_NO from EMPLOYEE_DETAILS")
for row in cursor:
 while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
       # cv2.rectangle(im,(x,y),(x+w,y+h),(127,255,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cursor = conn.execute("SELECT ID, NAME, GENDER, DESIGNATION, SHIFT, CONTACT_NO from EMPLOYEE_DETAILS")
        for row in cursor:
         if(conf<50):
            if(Id==row[0]):
               now = datetime.datetime.now()
               
               """ conn = sqlite3.connect('Timestamp_Data.db')
               print "Opened database successfully";"""
               now = datetime.datetime.now()
               conn1.execute("INSERT INTO TS_DATA3 (TS_ID,NAME,DATE, TIME,D_YEAR,D_MONTH,D_DAY )Values (?,?,?,?,?,?,?)",(str(Id),str(row[1]),now.strftime("%Y-%m-%d "),now.strftime("%H:%M"),now.strftime("%Y"),now.strftime("%m"),now.strftime("%d")))
               print "record added successfully"
               conn1.commit()
              # print "Records created successfully";
               cv2.waitKey(10000)==ord('p')
                 
               conn.close
               conn1.close
                       #MessageBox('FACE RECOGNITION', 'id:'+str(row[0])+'\nName:'+str(row[1])+'\nGender:'+str(row[2])+'\nDESIGNATION:'+str(row[3])+'\nSHIFT:'+str(row[4])+'\nContact_No:'+str(row[5])+'\n'+now.strftime("%d-%m-%Y %H:%M")  , 64)
         else:
            Id="Unknown"
            cv2.putText(im,str(Id),(x,h), font, 1,(255,255,255),2)
        
        
    
    cv2.imshow('im',im) 
    if cv2.waitKey(100)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()

