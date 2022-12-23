#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
from sense_hat import SenseHat
import logging
from dotenv import dotenv_values
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_mail(eFrom, to, subject, text):
    # SMTP Server details: update to your credentials or use class server
    smtpServer='smtp.mailgun.org'
    smtpUser='postmaster@sandbox333df02f7ff54c368b27efc8e20b7867.mailgun.org'
    smtpPassword='8e7b54342f87b6e24328ce29da561bb2-bdb2c8b4-d48f2a1b'
    port=587

    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msg['Subject'] = subject

    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()

dt = time.localtime()
currentTime = time.strftime("%H:%M:%S", dt) 

emailSent = False
openText= f'Open your window to lower the temperature: {currentTime}'
closeText= f'You can close your window now: {currentTime}'

# SenseHAT object
sense = SenseHat()

#load MQTT configuration values from .env file
config = dotenv_values(".env")

#configure Logging
logging.basicConfig(level=logging.INFO)

# Define event callbacks for MQTT
def on_connect(client, userdata, flags, rc):
    logging.info("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    logging.info("Message Sent ID: " + str(mid))

mqttc = mqtt.Client(client_id=config["clientId"])

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Configure MQTT client with user name and password
mqttc.username_pw_set(config["username"], config["password"])

# Connect to MQTT Broker
mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

# Set Thingspeak Channel to publish to
topic = "channels/"+config["channelId"]+"/publish"

# Publish a message at intervals
highTempEmail = False

while True:
    try:
        temp = round(sense.get_temperature_from_pressure(),2)
        humidity = round(sense.humidity,2)
        payload=f"field1={temp}&field2={humidity}"
        mqttc.publish(topic, payload)
        if temp > 16 and emailSent == False:
            send_mail('darraghc23@gmail.com', '20099857@mail.wit.ie', 'Open window', openText)
            emailSent = True
        elif temp <= 16 and emailSent == True:
            send_mail('darraghc23@gmail.com', '20099857@mail.wit.ie', 'Close window', closeText)
            emailSent = False
        time.sleep(int(config["transmissionInterval"]))
    except:
        logging.info('Interrupted')



#import board
#import adafruit_dht

#Initialize temp and humid sensor
#dhtDevice = adafruit_dht.DHT11(board.D17)

#while True:
#    try:
#        temp= dhtDevice.temperature
#        humidity = dhtDevice.humidity
#        payload=f"field1={temp}&field2={humidity}"
#        mqttc.publish(topic, payload)
#        time.sleep(int(config["transmissionInterval"]))
#    except:
#        logging.info('Interrupted')