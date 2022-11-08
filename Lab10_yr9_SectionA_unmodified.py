from djitellopy import Tello 
import cv2 

import time

tello = Tello()
tello.connect()



x=int(input("Enter the number of flips:\n"))
print("You have entered "+x+" number of flips")

for y in range (x):
       tello.flip(“f”)
