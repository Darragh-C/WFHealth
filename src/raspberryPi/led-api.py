#!/usr/bin/python3

from flask import Flask, request
from flask_cors import CORS
from gpiozero import LED
from time import sleep

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

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)