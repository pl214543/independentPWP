# https://stackoverflow.com/questions/41253939/how-to-create-array-of-frames-from-an-mp4-with-opencv-for-python

# required libraries
import cv2
import numpy as num

frames = []

recording = "IMG_1791.mp4"

video = cv2.VideoCapture(recording)

if video.isOpened() == False:
    print("Error opening video.")

# this is for shuffling through the frames
currentFrame = video.get(cv2.CAP_PROP_POS_FRAMES)

# runs ony when the video capture is open
while (video.isOpened()):
    booleanReady, frame = video.read()

    if booleanReady == True:

        # this creates a new variable for the frame to be appended to an array
        saveFrame = cv2.imread('video', frame)

        # this appends this save variable to the numpy array
        frame.append(saveFrame)

        # gets the next frame ready
        currentFrame = video.get(cv2.CAP_PROP_POS_FRAMES)

    else:

        # in case the previous frame didn't load, it goes back to it
        video.set(cv2.CAP_PROP_POS_FRAMES, currentFrame-1)

        # gives it a little time to load
        cv2.waitKey(1000)

    # checks if the current frame is the last frame
    if video.get(cv2.CAP_PROP_POS_FRAMES) == video.get(cv2.CAP_PROP_FRAME_COUNT):

        # stop
        break

    # # makes it grayscale so that the hough circles method works
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # blurring the video so that the can is more prominent than the background
    # blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # # median blurring
    # median = cv2.medianBlur(blurred, 5)
    # # uses hough circle on the most recent version of the video
    # houghCircle = cv2.HoughCircles(median, cv2.HOUGH_GRADIENT,
    #                                1, 20, param1=50, param2=30, minRadius=1,
    #                                maxRadius=40)
