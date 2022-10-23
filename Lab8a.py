from djitellopy import Tello
import time
import cv2

tello=Tello()
tello.connect()

time.sleep(5)
tello.takeoff()
tello.forward(20)
tello.right(20)
tello.up(5)

for x in range (3):       
    tello.flip("f")  
tello.stop
time.sleep(5)
tello.backward(20)
tello.left(20)
tello.down(5)

    tello.land()
