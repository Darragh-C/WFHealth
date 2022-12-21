import storeFBData
import json
from time import sleep
import datetime
import storeFBData

sleep_time = 15

def check_appliance_pwr_usg(appliance, interval):
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("appliances.json") as file:
        data = json.load(file)
        with open('appliances.json', 'r') as file:
            data = json.load(file)
            for obj in data["appliances"]:
                for key, val in obj.items():
                    if (key == "appliance") and (val == f"{appliance}"):
                        if obj["power"] == "on": 
                            joules = obj["joules"]*interval
                            print(f'{appliance} using {joules} J at {currentTime}') 
                            storeFBData.push_db_pwr_usg(appliance, joules, currentTime)
                            print('Data stored in db')


while True:
    check_appliance_pwr_usg("heater", sleep_time)
    check_appliance_pwr_usg("dehumidifier", sleep_time)
    sleep(sleep_time)