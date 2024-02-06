# https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

# import required libraries
import cv2
import numpy as num

# imports the video capture (should work)
from main import video

# this is here for reference does not function yet
grey = cv2.cvtColor(video, cv2.BGR2GRAY)
blurred = cv2.GaussianBlur(grey, (1, 1), 0)
canny = cv2.Canny(blurred, 100, 200)
