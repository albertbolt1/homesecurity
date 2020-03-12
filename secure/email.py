import cv2, time, pandas  
from datetime import datetime 
import urllib.request
import numpy as np
import smtplib
import os
def motiondetection():
    static_back = None
    motion_list = [ None, None ]     
    time1 = [] 
    df = pandas.DataFrame(columns = ["Start", "End"]) 
    url="http://192.168.43.1:8080/shot.jpg"

    video = cv2.VideoCapture(0) 
    oupath="C:/Users/albertbolt/sit/roytuts/gallery/media/motiondetection/"

    count=0
    a=True
    while (a): 
    
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp,-1)
        time.sleep(2)
        motion = 0
  

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  

        gray = cv2.GaussianBlur(gray, (21, 21), 0) 
 
        if static_back is None: 
            static_back = gray 
            continue
  

        diff_frame = cv2.absdiff(static_back, gray) 
  

        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1] 
        thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 
   
 
        (cnts, _) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
  
        for contour in cnts: 
            if cv2.contourArea(contour) < 10000: 
                continue
            motion +=1;
  
        (x, y, w, h) = cv2.boundingRect(contour) 
      
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3) 

        motion_list.append(motion) 
  
        motion_list = motion_list[-2:]  
        key = cv2.waitKey(1) 
      
  
         
        if motion_list[-1] == 1 and motion_list[-2] == 0: 
            time1.append(datetime.now()) 
    
    
        if motion_list[-1] == 0 and motion_list[-2] == 1: 
            time1.append(datetime.now()) 
        if (motion>2):
            
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login("namelessme49@gmail.com", "rememberguy841")
            server.sendmail("namelessme@gmail.com", "albertboltinfinity@gmail.com","there is some illegal activity in ur house please contact the police")
            server.quit()
            a=False
            