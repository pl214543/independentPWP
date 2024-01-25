# Set imread of opencv to the downloaded image
# using canny edge, hough, etc.
# get a fixed point in the center

# required libraries
import cv2
import numpy as num

# image name so that the image can be taken from pycharm project files.
# might need to be changed to a path if using terminal
imageName = "can2.png"
newImageName = "canCircle.jpg"

# defines the image needed
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

# makes the image grey for easier detection
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# blur the grey image
blurred = cv2.blur(grey, (1, 1))

# employs the use of hough circles (cv2 predefined method)
houghCircle = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT,
                               1, 20, param1=50, param2=30, minRadius=0,
                               maxRadius=0)

# if the circle created exists, common error when nothing is detected as none, so it flags errors
if houghCircle is not None:

    # rounds the numbers to an unassigned long of 16 using numpy
    houghCircle = num.uint16(num.around(houghCircle))

    # gets points a and b, and the radius that are needed to graph the circle
    for point in houghCircle[0, :]:
        a, b, r = point[0], point[1], point[2]

        # creates the actual circle using the original image, points a and b, radius
        # original image, center coordinates, radius, color, thickness
        # the color is in bgr, so the g for green is set
        cv2.circle(image, (a, b), r, (0, 255, 0), 10)

        # does the same but changes the radius to 1 so that there is a center dot.
        # the color is in bgr so the r for red is set
        cv2.circle(image, (a, b), 1, (0, 0, 255), 10)

        # displays the new image with overlay in a window named "Circle"
        cv2.imshow("Circle", image)

        cv2.imwrite(newImageName, image)

        # image closes after any key is pressed
        cv2.waitKey(0)
