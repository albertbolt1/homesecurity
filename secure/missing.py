import numpy as np
import os
import cv2
def missing():
	a=[]
	count=0
	path = "C:/Users/albertbolt/Create-Face-Data-from-Images/images/"
	outpath="C:/Users/albertbolt/Create-Face-Data-from-Images/missingitems/"
	for i in os.listdir(path):
    	i2= os.path.join(path, i)
    	a.append(i2)
	for i in range(len(a)-1):
    	image1 = cv2.imread(a[i])  
    	image2 = cv2.imread(a[i+1]) 
    	sub = cv2.subtract(image1, image2)
    	count1=str(count)+".jpg"
    	cv2.imwrite(os.path.join(outpath ,count1),sub)
    	count=count+1