from sense_hat import SenseHat
import logging
import socket
from time import sleep
from dotenv import dotenv_values

# Load .env file values
config = dotenv_values(".env")

logging.basicConfig(level=logging.INFO)

# SenseHAT object
sense = SenseHat()

# UDP client config parameters
serverAddressPort = (config["ipAddress"], int(config["port"]))
deviceID = config["deviceID"]
interval = int(config["transmissionInterval"])

# Client side UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

logging.info(f"Listening for UDP Datagrams on port: {serverAddressPort}")

while True:
    temperature = round(sense.temperature,2)
    humidity = round(sense.humidity,2)
    msgFromClient = {"deviceID": deviceID,"temp":temperature,"humidity":humidity}
    bytesToSend = str(msgFromClient).encode()
    # Send to server on UDP socket (UDPClientSocket)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)      
    # Console log
    logging.info("Sent to server: " + str(msgFromClient))
    # Sleep for interval before next transmission 
    sleep(interval)