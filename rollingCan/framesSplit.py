# required libraries
import cv2
import numpy as num

# gets the opencv video capture into this file
from main import video

# array for the frames
frames = []

# this is for shuffling through the frames
currentFrame = video.get(cv2.CAP_PROP_POS_FRAMES)

# runs ony when the video capture is open
while (video.isOpened()):
    booleanReady, frame = video.read()

    # to check if the frames exist
    if booleanReady == True:

        # this appends this the frame to the numpy array
        frames.append(frame)

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

# opens the next file to write the circles onto each frame
import houghWriting
