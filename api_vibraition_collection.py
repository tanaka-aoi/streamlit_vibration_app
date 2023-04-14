import requests
import pandas as pd
import os
import glob
import csv
from csv import writer
import numpy as np
import json
import datetime

res = requests.get('https://b53pwk08u9.execute-api.ap-northeast-1.amazonaws.com/myiot-stage/get?connectorId=c4ce7171-7742-46b8-b6d1-51fc9f14b2ca&edgeId=70:87:A7:FC:B8:31')

# print(res.status_code)
# print(res.text)
# print(res.json())
vibration_json = res.json()
vibration = vibration_json['data']['thi']
print(vibration)
# print(vibration['data']['thi'])

# os.chdir('C:/Users/pcsysmane/Documents/04_MyIoT/20230405_Qriot_conan_myiot_system/03_app_dev/npc_app')
with open('./data/data.csv', 'a') as csvFile:
    writer = csv.writer(csvFile, lineterminator="\n")
    
    datalist = []

    # 日付取得
    dt_now = datetime.datetime.now()
    date = dt_now.strftime('%Y/%m/%d %H:%M')
    datalist.append(date)

    # 振動値
    datalist.append(vibration)

    # writer = csv.writer(csvFile)
    writer.writerow(datalist)
    # print(datalist)
csvFile.close()
print('end')
cwd = os.getcwd()
print(cwd)
