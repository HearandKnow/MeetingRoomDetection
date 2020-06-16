# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:48:05 2020

@author: Jeremy
"""
import cv2
import numpy as np

print("Utils.py loaded")

"""
Camera setting, depends of how many cameras you have connected to the computer
"""
Camera = 1

"""
ERROR function
param : msg (string)

Print error message from which file plus custom message
"""
def ERROR(msg):
    print("From Utils.py : "+str(msg))


"""
openCamera function
param : device (int)

Set up the camera capture device 

return cap as capture device and the Camera id used
"""
def openCamera(device):
    try:
       Camera = device
       cap = cv2.VideoCapture(Camera)
       return cap, Camera
    except:
        cap.relase()
        ERROR("Can't open camera")
    

"""
takePic function
param : name_of_pic (string)

Take a picture and save it to the main folder as jpg
To save it to a specific folder, you can write the path with '//' as name_of_pic
example : name_of_pic = C://Users//HandK//Desktop//the_name_of_my_pic
"""
def takePic(name_of_pic):
    cap, _ = openCamera(Camera)
    try:
       s, im = cap.read() # captures image
       name_of_pic = str(name_of_pic)
       cv2.imwrite(name_of_pic+".jpg",im) # writes image test.jpg to disk
       cap.release()
    except:
        ERROR("Can't write pic "+name_of_pic)
       

"""
film function

Used to test if camera works
"""
def film():
    cap, _ = openCamera(Camera)
    try:
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Display the resulting frame
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
    except:
        ERROR("Camera isn't working")
        
        

"""
testExposure function
param : num_expo (int) between -1 and -13

Test differents exposures for the camera (if the camera is compatible)

-1	640 ms
-2	320 ms
-3	160 ms
-4	80 ms
-5	40 ms
-6	20 ms
-7	10 ms
-8	5 ms
-9	2.5 ms
-10	1.25 ms
-11	650 µs
-12	312 µs
-13	150 µs
"""
def testExposure(num_expo):
    try:
        num_expo = int(num_expo)
        if num_expo < -13 or num_expo > -1:
            raise
    except:
        ERROR("Please enter a number between -1 and -13")
    cap, _ = openCamera(Camera)
    try:
        cap.set(cv2.CAP_PROP_EXPOSURE,num_expo)  
        while(True):
            ret, frame = cap.read()    
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    except:
        ERROR("Camera isn't working")
