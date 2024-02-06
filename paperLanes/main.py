# NEED TO CITE CODE
# https://uark.libguides.com/CSCE/CitingCode
# https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
# cv2.line(image, start_point, end_point, color, thickness)
# have a programming plan and glossary + technical algorithm

# import required libraries
import cv2
import numpy as num

video = cv2.VideoCapture(0)

def checkVideo(video):
    if video.isOpened():
        print("Video will not open.")

checkVideo(video)

import detectLines
