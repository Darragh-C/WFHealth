from sense_hat import SenseHat
import datetime
import storeFBData
from time import sleep

# SenseHAT object
sense = SenseHat()

while True:
    temp = round(sense.temperature,2)
    humid = round(sense.humidity,2)
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # print temp, humid, and time to console
    print(f'temp {temp} and humid {humid} recorded at {currentTime}') 
    storeFBData.push_db_temp_humid(temp, humid, currentTime)
    print('Data stored in db')
    sleep(15)