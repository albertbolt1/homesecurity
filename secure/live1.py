import cv2
import numpy as np
import urllib.request
import os
import time




def foo():
    abort_after = 50
    start = time.time()
    delta = time.time() - start
    
    url="http://192.168.43.1:8080/shot.jpg"
    scaling_factor =0.75
    cap = cv2.VideoCapture(0)
    count=0
    while True:
        imglink=urllib.request.urlopen(url)
        imgNp=np.array(bytearray(imglink.read()))
        time.sleep(10)
        img = cv2.imdecode(imgNp,-1)
        path = "C:/Users/albertbolt/sit/roytuts/gallery/media/images/"
        path1="C:/Users/albertbolt/sit/roytuts/gallery/media/images/thumbs/"
        count1=str(count)+".jpg"
        cv2.imwrite(os.path.join(path ,count1), img)
        cv2.imwrite(os.path.join(path1 ,count1), img)
        count=count+1
        if(delta >= abort_after):
            break
        cap.release()
        cv2.destroyAllWindows()
