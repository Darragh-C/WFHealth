import socket
import RPi.GPIO as GPIO
import board
import neopixel


GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)

pixels1 = neopixel.NeoPixel(board.D18, 150, brightness=0.1)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port=1235
serverSocket.bind(('', port))
print("Server listening on port "+ str(port))
while True:
    message, address = serverSocket.recvfrom(1024)
    print(message)
    if str(message) == "b'dark'":   
        pixels1.fill((255, 255, 255))
    else:
        pixels1.fill((0, 0, 0))