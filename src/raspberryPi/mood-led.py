import time
import board
import neopixel
import sys

pixels1 = neopixel.NeoPixel(board.D18, 150, brightness=1)



if sys.argv[1] == "white":
    pixels1.fill((255, 255, 255))
elif sys.argv[1] == "green":
    counter=0
    while counter < 150:
        pixels1[counter] = (0, 255, 0)
        counter+=1
elif sys.argv[1] == "red":
    counter=0
    while counter < 150:
        pixels1[counter] = (255, 0, 0)
        counter+=1
elif sys.argv[1] == "blue":
    counter=0
    while counter < 150: 
        pixels1[counter] = (0, 0, 255)
        counter+=1
elif sys.argv[1] == "yellow":
    counter=0
    while counter < 150: 
        pixels1[counter] = (255, 150, 0)
        counter+=1
elif sys.argv[1] == "orange":
    counter=0
    while counter < 150: 
        pixels1[counter] = (255, 30, 0)
        counter+=1
elif sys.argv[1] == "purple":
    counter=0
    while counter < 150: 
        pixels1[counter] = (191, 0, 191)
        counter+=1
else: 
    pixels1.fill((0, 0, 0))