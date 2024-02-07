# NEED TO CITE CODE
# https://uark.libguides.com/CSCE/CitingCode
# https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
# cv2.line(image, start_point, end_point, color, thickness)
# have a programming plan and glossary + technical algorithm
# dodge and burn
# field of view
# maybe grayscale and then remove all darker colors (+ dodge and burn)
# https://www.geeksforgeeks.org/filter-color-with-opencv/
# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/ for capturing video and editing

# import required libraries
import cv2
import numpy as num

video = cv2.VideoCapture(0)

def checkVideo(video):
    if video.isOpened():
        print("Video will not open.")

checkVideo(video)

# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
while True:
    booleanReady, frame = video.read()

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(grey, (1, 1), 0)
    # canny = cv2.Canny(blurred, 100, 200)

    # https://www.geeksforgeeks.org/filter-color-with-opencv/
    ranged = cv2.inRange(blurred, 125, 255)
    result = cv2.bitwise_and(blurred, blurred, mask=ranged)

    cv2.imshow('Frame', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# import detectLines

