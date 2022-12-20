import BlynkLib
import board
import adafruit_dht
import logging
from time import sleep
# Load .env file values
config = dotenv_values(".env")

# Blynk credentials
BLYNK_TEMPLATE_ID = config["BLYNK_TEMPLATE_ID"]
BLYNK_DEVICE_NAME = config["BLYNK_DEVICE_NAME"]

# Initialize Blynk
blynk = BlynkLib.Blynk(config["BLYNK_AUTH_TOKEN"])

#Initialize temp and humid sensor
dhtDevice = adafruit_dht.DHT11(board.D17)

# Event listener
while True:
    try:
        blynk.run()
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        blynk.virtual_write(1, temperature)
        blynk.virtual_write(1, humidity)
     except RuntimeError as error:    
         logging.error(error.args[0])
    sleep(15) 