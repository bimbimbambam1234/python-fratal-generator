import serial
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
comPort = 'COM16'
baudrate = 9600
uno = serial.Serial(comPort,baudrate)
low_red= (6,102,255)
high_red= (255,255,255)
low_green= (51,121,62)
high_green= (84,255,255)
low_blue= (64,0,255)
high_blue= (114,255,204)

while True:
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_green=cv2.inRange(frame,low_green,high_green)
    mask_red=cv2.inRange(frame,low_red,high_red)
    mask_blue=cv2.inRange(frame,low_blue,high_blue)
    color_red=np.count_nonzero(mask_red)
    color_green=np.count_nonzero(mask_green)
    color_blue=np.count_nonzero(mask_blue)
    if color_red>1000:
        uno.write(b'1')
    elif color_green>1000:
        uno.write(b'2')
    elif color_blue>1000:
        uno.write(b'3')
    else: uno.write(b'0')
    cv2.imshow("mask_green", mask_green)
    cv2.imshow("mask_red", mask_red)
    cv2.imshow("mask_blue", mask_blue)
    cv2.imshow("original", frame)
    cv2.waitKey(1)