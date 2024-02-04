# import required libraries
import cv2
import numpy as num

# imports the final array of edited frames
from houghWriting import newFrames

# gets the height and width of the original frames for the video
height,width,layers=newFrames[1].shape

# sets up an MP4 video file for saving named "finalVideo.mp4"
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
finalVideo = cv2.VideoWriter('finalVideo.mp4', fourcc, 20.0, (width, height))

# every frame in the final array
for frame in newFrames:
    frameFinal = frame

    # writes each frame to the video
    finalVideo.write(frameFinal)

# finally closes everything
cv2.destroyAllWindows()
finalVideo.release()
