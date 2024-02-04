# required library
import cv2
import numpy as num

# imports the array of frames and the video capture object
from framesSplit import video, frames

# makes an array for the edited frames
newFrames = []

# a frame counter
count = 1

# each frame in the frames array
for frame in frames:
    # to keep track of the frames
    print("Frame " + str(count))
    count += 1

    # writes the frame to an image for retrieval
    cv2.imwrite("video.jpg", frame)

    # retrieves the frame for editting
    frameSave = cv2.imread("video.jpg", cv2.IMREAD_COLOR)

    # turns the image grey for easier circle detection.
    grey = cv2.cvtColor(frameSave, cv2.COLOR_BGR2GRAY)

    # blurs the image using GaussianBlur for easier circle detection
    blurred = cv2.GaussianBlur(grey, (1, 1), 0)

    # detects the circles
    # min distance is set to 2000 so that no more than one circle are added
    # param for more accurate circle detection
    # minimum radius is so that only the outer circle is detected.
    houghCircle = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT,
                                   1, 2000, param1=29, param2=87, minRadius=250,
                                   maxRadius=0)

    # checks if the houghCircle is detected at all
    if houghCircle is not None:
        houghCircle = num.uint16(num.around(houghCircle))

        # every point
        for point in houghCircle[0, :]:

            # for testing purposes
            print("point")
            # gets points a and b and the radius for drawing the circle
            a, b, r = point[0], point[1], point[2]

            # prints the radius for testing and minimum radius
            print(r)

            # creates the actual circle using the original image, points a and b, radius
            # original image, center coordinates, radius, color, thickness
            # the color is in bgr, so the g for green is set
            cv2.circle(frameSave, (a, b), r, (0, 255, 0), 10)

            # does the same but changes the radius to 1 so that there is a center dot.
            # the color is in bgr so the r for red is set
            cv2.circle(frameSave, (a, b), 1, (0, 0, 255), 10)

            # saves the image to file name "newFrame.jpg" in order to save to an array
            cv2.imwrite("newFrame.jpg", frameSave)

            # adds the frame to the array
            newFrames.append(frameSave)

    else:
        # adds the frame to the array even if no circles are found
        newFrames.append(frameSave)

# opens the file that actually writes the video
import finalVideo
