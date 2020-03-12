import pandas as pd
import pyautogui
def battery():
    a=True
    while(a):
        a=[]
        dp=pd.read_json("http://192.168.43.1:8080/sensors.json")
        e=dp['battery_level']['data']
        for i in range(0,len(e)):
            for b in e[i][1]:
                a.append(b)
        for i in range(0,len(a)):
            if(i<70):
                pyautogui.alert('ur webcam battery is going low ', "Title")
                a=False
            