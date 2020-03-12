import pandas as pd
import pyautogui
import time
def light():
    a=True
    b=[]
    while(a):
        a=[]
        dp=pd.read_json("http://192.168.43.1:8080/sensors.json")
        time.sleep(10)
        e=dp['battery_level']['data']
        a=dp['light']['data']
        sum=0
        for i in range(len(a)):
            sum=sum+a[i][1][0]
        sum1=sum/len(a)
        b.append(sum1)
        if((b[len(b)-1]-b[len(b)-2])>20):
            pyautogui.alert('there is some illegal activity going on in the house', "Title")
            a=False
        