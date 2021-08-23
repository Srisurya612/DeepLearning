from PIL import Image
from gtts import gTTS

# ocr import
import os
import pytesseract
import subprocess
from subprocess import *
#import picamera
import numpy as np
import cv2
import pyttsx3
import datetime
#switch import
#import RPi.GPIO as GPIO
import time
import imutils
#from picamera import PiCamera
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
mode = input()

while True:
    #if (GPIO.input(13) and GPIO.input(15)):
    if mode=='Object Detection':
        print("Press for Objectect detection")
        Popen(["python",r"C:\Users\ASUS\Desktop\DEEp\models\research/Project369.py"])
    #elif GPIO.input(11):
    #elif mode=='OCR':

     #   print("Press for text to speech")     
      #  try:
       #     call(["python3","tts.py"])
        #except:
         #   print("error occured in OCR")
    #elif GPIO.input(13):
    elif mode=='Facial Recognition':
        

        print("Press for Face recognition")
        try:
            print("call")
            subprocess.Popen(["python",r"Endproduct1.py"],stdout=PIPE,stderr=PIPE)
        except:
            print("error occured in Face recognition")

    #elif GPIO.input(15):
    elif mode == 'Pedestrian':
        print('Press for Pedestrian Detection')
        try:
            print('CAll')
            subprocess.Popen(['python',r'C:\Users\ASUS\Desktop\DEEp\MY PROJECT\human/human_detect.py'],stdout=PIPE,stderr=PIPE)
        except:
            print('error occured in Pedestrian detection')
     #   print("Press for yellow path")
      #  try:
       #     print("call")
        #    call(["python3","yellowPath.py"])
        #except:
         #   print("error occured in yellow path")
    else:
        print("No click")
    time.sleep(20)

