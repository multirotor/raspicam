#!/usr/bin/env python
# -*- coding: utf-8 -*-
# returns HSV value of the pixel under the cursor in a video stream
# author: achuwilson
# achuwilson.wordpress.com
import cv2
import time

def on_mouse(event,x,y,flag,param):
  if(event==cv2.EVENT_LBUTTONDOWN):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    s = hsv[y, x]
    print "H:",s[0],"      S:",s[1],"       V:",s[2]

cv2.namedWindow("camera", 1)
camera = cv2.VideoCapture(0)
cv2.setMouseCallback("camera",on_mouse, 0);

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    frame = cv2.blur(frame, (3, 3))
    cv2.imshow("camera", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# close camera and any open windows
camera.release()
cv2.destroyAllWindows()
