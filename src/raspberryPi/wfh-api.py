#!/usr/bin/python3

from flask import Flask, request
from flask_cors import CORS
from gpiozero import LED
from time import sleep
import json

led = LED(18)

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

@app.route('/light',methods=['POST'])
def light_post():
    state=request.args.get('state')
    print (state)
    if (state=="on"):
        led.on()
        return '{"state":"on"}'
    else: 
        led.off()
        return '{"state":"off"}'

@app.route('/heater', methods=['POST'])
def heater_power():
    power=request.args.get('power')
    if (power=="on"):
        with open('temp-humid-fb/appliances.json', 'r') as file:
            data = json.load(file)  
            for obj in data["appliances"]:
                for key, val in obj.items():
                    if (key == "appliance") and (val == "heater"):
                        obj["power"] = "on"
        with open('temp-humid-fb/appliances.json', 'w') as file:
            json.dump(data, file, indent=4) 
        return '{"power":"on"}'
    elif (power=="off"):
        with open('temp-humid-fb/appliances.json', 'r') as file:
            data = json.load(file)
            for obj in data["appliances"]:
                for key, val in obj.items():
                    if (key == "appliance") and (val == "heater"):
                        obj["power"] = "off"  
        with open('temp-humid-fb/appliances.json', 'w') as file:
            json.dump(data, file, indent=4) 
        return '{"power":"off"}'
    else:
        return 'not recognised'

@app.route('/dehumid', methods=['POST'])
def dehumid_power():
    power=request.args.get('power')
    if (power=="on"):
        with open('temp-humid-fb/appliances.json', 'r') as file:
            data = json.load(file)
            for obj in data["appliances"]:
                for key, val in obj.items():
                    if (key == "appliance") and (val == "dehumidifier"):
                        obj["power"] = "on"   
        with open('temp-humid-fb/appliances.json', 'w') as file:
            json.dump(data, file, indent=4) 
        return '{"power":"on"}'
    elif (power=="off"):
        with open('temp-humid-fb/appliances.json', 'r') as file:
            data = json.load(file)
            for obj in data["appliances"]:
                for key, val in obj.items():
                    if (key == "appliance") and (val == "dehumidifier"):
                        obj["power"] = "off"     
        with open('temp-humid-fb/appliances.json', 'w') as file:
            json.dump(data, file, indent=4) 
        return '{"power":"off"}'
    else:
        return 'not recognised'

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)