import numpy as np
import os
import cv2
import time
def substract():
    a=[]
    count=0
    t = time.localtime()
    current_time = time.strftime("%H", t)
    current_time = int(current_time)
    path = "C:/Users/albertbolt/Create-Face-Data-from-Images/images/"
    if(current_time==17):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems18/"
    elif(current_time==19):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems19/"
    elif(current_time==20):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems20/"
    elif(current_time==21):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems21/"
    elif(current_time==22):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems22/"
    elif(current_time==23):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems23/"
    elif(current_time==24):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems24/"
    elif(current_time==14):
        outpath="C:/Users/albertbolt/sit/roytuts/gallery/media/missingitems14/"
        
    outpath1=outpath+"thumbs/"
    for i in os.listdir(path):
        i2= os.path.join(path, i)
        a.append(i2)
    for i in range(len(a)-1):
        image1 = cv2.imread(a[i])  
        image2 = cv2.imread(a[i+1]) 
        sub = cv2.subtract(image1, image2)
        count=count+1
        diff = cv2.absdiff(image1, image2)
        mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        th = 1
        imask =  mask>th
        canvas = np.zeros_like(image2, np.uint8)
        canvas[imask] = image2[imask]
        count1=str(count)+".jpg"
        cv2.imwrite(os.path.join(outpath ,count1),sub)
        cv2.imwrite(os.path.join(outpath1 ,count1),sub)