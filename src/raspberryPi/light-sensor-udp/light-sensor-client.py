
import logging
import socket
from time import sleep
from dotenv import dotenv_values
import board
#import adafruit_dht
import RPi.GPIO as GPIO

# Load .env file values
config = dotenv_values(".env")

logging.basicConfig(level=logging.INFO)

#Initialize temp and humid sensor
#dhtDevice = adafruit_dht.DHT11(board.D17)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

# UDP client config parameters
serverAddressPort = (config["ipAddress"], int(config["port"]))
deviceID = config["deviceID"]
interval = int(config["transmissionInterval"])

# Client side UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

logging.info(f"Listening for UDP Datagrams on port: {serverAddressPort}")

while True:
    #temperature= dhtDevice.temperature
    #humidity = dhtDevice.humidity
    brightness = ""
    if GPIO.input(16) == 1:
        brightness = "dark"
    else:
        brightness = "light"
    msgFromClient = brightness
    #msgFromClient = {"deviceID": deviceID,"temp":temperature,"humidity":humidity}
    bytesToSend = str(msgFromClient).encode()
    # Send to server on UDP socket (UDPClientSocket)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)      
    # Console log
    logging.info("Sent to server: " + str(msgFromClient))
    # Sleep for interval before next transmission 
    sleep(interval)