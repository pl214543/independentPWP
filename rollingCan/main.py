# Plan
# Turn video into many frames and save each frame into an array
# Put houghcircles onto each frame
# Add all of these edited frames into a new array
# put all of these frames together to make a new and final video

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

    print(type(frame))
    print(frame)

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

print("\n\n\n\n\n\n\n\n\nTest\n\n\n\n\n\n\n\n")
print(len(frames))
print(frames[45])
video = cv2.imwrite("video.jpg", frames[90])

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
