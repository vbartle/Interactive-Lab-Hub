import cv2
import time
import numpy as np

capture = cv2.VideoCapture(0)
while True:
    success, img = capture.read()
    cv2.imshow("img", img)
    cv2.waitKey(1)