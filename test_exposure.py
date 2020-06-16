# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:35:37 2020

@author: Jeremy
"""
print("Hear&Know Software")

import cv2
import numpy as np
from Utils import openCamera

"""
Set up the camera
"""

cap, _ = openCamera(1)

"""
ERROR function
param : msg (string)

Print error message from which file plus custom message
"""
def ERROR(msg):
    print("From test_exposure.py : "+str(msg))


def detectionInfectedArea():
    
    last_image, dist_image, c, res = 0, 0, 0, 0
    ret, original = cap.read()
    
    cv2.imwrite("original.jpg",original)
    
    if cap.isOpened():
        last_image = np.zeros([int(cap.get(4)),int(cap.get(3))],np.uint8)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        gray_image = cv2.Canny(gray_image,10,150)

        if c == 1:
            dist_image += np.asarray(abs(np.float32(gray_image) - np.float32(last_image)))
        
        last_image = gray_image

        res = dist_image
        c=1
        # Display the resulting frame
        cv2.imshow('res',last_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    norm_dist = cv2.normalize(res, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    cv2.imwrite("dist.jpg",norm_dist)
    norm_dist = cv2.cvtColor(norm_dist,cv2.COLOR_GRAY2BGR)
    result = norm_dist + original
    cv2.imwrite("res.jpg",result)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
    
detectionInfectedArea()