import BlynkLib
from sense_hat import SenseHat
from time import sleep
# Load .env file values
config = dotenv_values(".env")

# Blynk credentials
BLYNK_TEMPLATE_ID = config["BLYNK_TEMPLATE_ID"]
BLYNK_DEVICE_NAME = config["BLYNK_DEVICE_NAME"]

# Initialize Blynk
blynk = BlynkLib.Blynk(config["BLYNK_AUTH_TOKEN"])

# Initialise SenseHAT
sense = SenseHat()
sense.clear()

# Event listener
while True:
    blynk.run()
    blynk.virtual_write(1, round(sense.temperature,2))
    blynk.virtual_write(1, round(sense.humidity,2))
    sleep(15) 