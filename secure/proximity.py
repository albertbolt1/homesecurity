import pandas as pd
import pyautogui
import time
def prox():
    a=True
    b=[]
    while(a):
        a=[]
        dp=pd.read_json("http://192.168.43.1:8080/sensors.json")
        a=dp['proximity']['data']
        time.sleep(1)
        if(a[0][1][0]==0.0):
            pyautogui.alert('someone is touching the device please check', "Title")
            a=False