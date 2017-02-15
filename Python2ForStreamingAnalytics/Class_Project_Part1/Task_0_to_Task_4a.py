import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# Task 2 & 3: Something is moving on the video - Part 1 and 2
import pandas as pd
# Open a video descriptor
feed_descriptor = cv2.VideoCapture('train_training.mp4')
# set variables and create empty lists
roi_thresh = 0.05
history = pd.DataFrame(columns=['Detected left', 'Detected right'])
history_length = 70
motion_fractions = []
motion_thresh = 35
running_avg = None
alpha = 0.2
while(feed_descriptor.isOpened()):
    # Read frame by frame
    current_frame = feed_descriptor.read()[1]

    if current_frame is not None:
        gray_current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        smooth_current_frame = cv2.GaussianBlur(gray_current_frame, (9, 9), 0)

        if running_avg is None:
            # If this is the first frame, set running_avg to current frame
            running_avg = np.float32(smooth_current_frame)

        else:
            # diff_frame is the absolute difference between the current frame and the running weighted average of previous frames
            diff_frame = cv2.absdiff(np.float32((smooth_current_frame)), np.float32((running_avg)))
            # Weights the current frame along with the previous frames
            cv2.accumulateWeighted(np.float32(smooth_current_frame), running_avg, alpha)
            # for all pixels above "motion_thresh" set to 1, otherwise set to 0
            _, subtracted = cv2.threshold(diff_frame, motion_thresh, 1, cv2.THRESH_BINARY)
            # motion_fraction is the percentage of pixels on the entire framethat are moving
            motion_fraction = (sum(sum(subtracted))/(subtracted.shape[0]*subtracted.shape[1]))
            motion_fractions.append(motion_fraction)
            print(motion_fraction)
   # Check if current frame is not different from NONE
    elif current_frame is None:
        break

# Plot the motion fractions/percent of pixels that change

plt.plot(np.array(motion_fractions))
plt.ylabel('Number of pixels that change')
plt.axis([0,60,0,0.3])
plt.show()
# Print a gray frame and a thresholded frame
cv2.imshow('Gray', gray_current_frame)
cv2.imshow('Thresholded difference', subtracted)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Task 4: Where this train goes?

# Task 4a: Define ROIs

# Display the two regions of interest
ROI = cv2.rectangle(smooth_current_frame, (400,400),(250,300),(0,255,0),3)
ROI2 = cv2.rectangle(ROI, (600,400),(450,300),(0,5,0),3)
cv2.imshow('ROI2', ROI2)
cv2.waitKey(0)
cv2.destroyAllWindows()

