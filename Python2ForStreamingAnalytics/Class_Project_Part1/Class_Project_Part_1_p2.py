import cv2
import numpy as np

# Task 0:
img = cv2.imread('mario3.png', cv2.IMREAD_COLOR)
# Apply the threshold function
ret,thresh = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
# display the image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 1a: Display Mario Gray-Scale

grayMario = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', grayMario)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 1b: Reducing the background noise of a video

blurMario = cv2.GaussianBlur(grayMario, (9,9), 0)
cv2.imshow('image', blurMario)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 1c: Image differencing
# Create the gray and blurry mario for mario2.png
img4 = cv2.imread('mario4.png', cv2.IMREAD_COLOR)
ret,thresh = cv2.threshold(img4, 127,255,cv2.THRESH_BINARY)
grayMario4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
blurMario4 = cv2.GaussianBlur(grayMario4, (9,9), 0)
cv2.imshow('image', blurMario4)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Use absdiff function to show the pixel differences from the two marios
diffMario = cv2.absdiff(np.float32((blurMario)), np.float32((blurMario4)))
cv2.imshow('image', diffMario)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Task 2: Something is moving on the video - Part 1

# number of pixels that have changed, compared to all pixels in picture

# 4 define ROI region of interest. define a small square
#measure when the first one moves and when the 2nd one moves
#5 recalibrate ROI, left to right or right to left
# Task 1: Preliminary understand about video processing
# Task 1a: Display Mario in Gray-scale
#cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
