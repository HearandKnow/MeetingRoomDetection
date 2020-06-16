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


"""
detectionInfectedArea function
Main program

Compute the sum of distance between pixels between each frame
"""
def detectionInfectedArea():
    
    # Initialization
    last_image, dist_image, skip_one, sum_dist = 0, 0, 0, 0 
    
    try:
        ret, original = cap.read() # Read camera 
        cv2.imwrite("original.jpg",original) # Save the first frame as the original set up of the room
    except:
        ERROR("Can't read or save 1st frame")
        
    try:
        if cap.isOpened():
            last_image = np.zeros([int(cap.get(4)),int(cap.get(3))],np.uint8) # Set up an empty frame for the first distance calculation
    except:
        ERROR("Can't set up an empty frame")
    
    # Main analysis
    try:
        while(True):
            
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            # Transform to gray pictures because we don't need colors
            gray_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            # Apply canny filter to avoid noise
            gray_image = cv2.Canny(gray_image,10,150)
    
            # Sum of distance calculation between each frame and avoid 1st frame
            if skip_one == 1:
                dist_image += np.asarray(abs(np.float32(gray_image) - np.float32(last_image)))
            skip_one=1
            
            # Save the previous frame
            last_image = gray_image
    
            sum_dist = dist_image
            
            # Display the resulting frame
            cv2.imshow('res',last_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except:
        ERROR("Can't sum the distance")
    
    try:
        # Normalization of the sum 
        norm_dist = cv2.normalize(sum_dist, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        
        # Save the norm_dist image
        cv2.imwrite("dist.jpg",norm_dist)
        
        # Put it back to 3 channels image for the overlap
        norm_dist = cv2.cvtColor(norm_dist,cv2.COLOR_GRAY2BGR)
        
        # Overlap the original and the norm_dist images
        result = norm_dist + original
        
        # Save result
        cv2.imwrite("res.jpg",result)
    except:
        ERROR("Can't compute the result")
    
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
    
    
detectionInfectedArea()