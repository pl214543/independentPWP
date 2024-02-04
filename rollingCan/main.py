# Plan
# Turn video into many frames and save each frame into an array
# Put houghcircles onto each frame
# Add all of these edited frames into a new array
# put all of these frames together to make a new and final video

# required libraries
import cv2
import numpy as num

# file name
recording = "IMG_1791.mp4"

# the video capture is set up for opencv2
video = cv2.VideoCapture(recording)

# checks if the video is active, and if it is not then it prints an error message
if video.isOpened() == False:
    print("Error opening video.")

# opens the file to splinter the video
import framesSplit
