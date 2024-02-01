# import required libraries
import cv2
import numpy as num

# video name
videoName = "TEMPLATE"

# video capture object
video = cv2.VideoCapture(videoName)

if not video.isOpened():
    print("Error opening video stream or file")

