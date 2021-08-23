import numpy as np
import cv2
from PIL import Image
import os
import pyttsx3
import datetime
haar_face = cv2.CascadeClassifier(r'C:\Users\ASUS\Desktop\DEEp\MY PROJECT\Classifiers/face.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r'C:\Users\ASUS\Desktop\DEEp\MY PROJECT\new_training.yml')
cam = cv2.VideoCapture(0)
label_predicted = 0
names = ['None','Surya','Srinu','Kasturi','Venkatamma','Raghavmma']
minW = 0.1*1080
minH = 0.1*720

while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = haar_face.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW),int(minH)),flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        r = (2*x+w)//2
        label_predicted, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        #cv2.rectangle(img,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        engine = pyttsx3.init()
        if (label_predicted==1):
            engine = pyttsx3.init()
            label_predicted = names[label_predicted]
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
        elif(label_predicted==2):
            label_predicted = names[label_predicted]
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
        elif(label_predicted==3):
            label_predicted = names[label_predicted]
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
        elif(label_predicted==4):
            label_predicted = names[label_predicted]
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
        elif(label_predicted==5):
            label_predicted = names[label_predicted]
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
        else:
            label_predicted = 'Unknown'
            engine.say('its'+str(label_predicted))
            engine.runAndWait()
            
            
            
        cv2.putText(img,str(label_predicted)+'--'+str(confidence),(x,y+h),cv2.FONT_HERSHEY_COMPLEX,1.1,(0,255,0))
    cv2.imshow('img',img)
    k = cv2.waitKey(10) & 0xff==ord('q')
    if k:
        break
print("\n[INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

