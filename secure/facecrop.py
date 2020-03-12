import cv2
import numpy as np
import urllib.request
from skimage.io import imsave
import time
cap = cv2.VideoCapture(0)
new_path = 'C:/Users/albertbolt/Anaconda3/Library/etc/haarcascades/'
face_cascade = cv2.CascadeClassifier(new_path + 'haarcascade_frontalface_default.xml')
url="http://192.168.43.1:8080/shot.jpg"
scaling_factor =0.75
path='C:/Users/albertbolt/sit/roytuts/gallery/media/images/thumbs'

def facecrop1():
    face=[]
    k1=0
    while True:
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        time.sleep(5)
        img = cv2.imdecode(imgNp,-1)
        frame = cv2.resize(img, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
        face_rects = face_cascade.detectMultiScale(frame, 1.3, 2)
        for (x,y,w,h) in face_rects:
            a=cv2.rectangle(frame, (x,y), (x+w,y+h), (3400,1234,2500), 5)   
            face.append(a)
        for i in face:
            k2=str(k1)+".jpg"
            imsave('C:/Users/albertbolt/sit/roytuts/gallery/media/facedetection/thumbs/'+k2,i)
            imsave('C:/Users/albertbolt/sit/roytuts/gallery/media/facedetection/'+k2,i)
            k1=k1+1
        
        
        cap.release()
        cv2.destroyAllWindows()