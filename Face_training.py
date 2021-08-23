import cv2
import numpy as np
import os
from PIL import Image
#path = os.path.dirname(os.path.abspath(__file__))
recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = r'D:\MY PROJECT\Classifiers\face.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
dataPath = r'D:\MY PROJECT\faces'

def getImagesAndLabels(dataPath):
    image_paths = [os.path.join(dataPath,f) for f in os.listdir(dataPath)]
    images=[]
    labels = []
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil,'uint8')
        label = int(os.path.split(image_path)[1].split(".")[0].replace('User-',''))

        #print(label)
        faces = faceCascade.detectMultiScale(image)
        for(x,y,w,h) in faces:
            images.append(image[y:y+h,x:x+w])
            labels.append(label)
            cv2.imshow('Appending faces...........', image[y:y+h,x:x+w])
            cv2.waitKey(10)
    return images,labels
images,labels = getImagesAndLabels(dataPath)
cv2.imshow('test',images[0])
cv2.waitKey(1)
recognizer.train(images, np.array(labels))
recognizer.write(r'new_training.yml')
cv2.destroyAllWindows()
print(labels[1])
