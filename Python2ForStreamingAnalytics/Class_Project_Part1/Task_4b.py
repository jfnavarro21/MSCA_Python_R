import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Task 4-b Use ROIs and apply the same function to dectect movement

# Open a video descriptor
feed_descriptor = cv2.VideoCapture('train_training.mp4')
# set variables and create empty lists
roi_thresh = 0.05
motion_fractions = []
motion_fractions2 = []
motion_thresh = 35
running_avg = None
running_avg2 = None
alpha = 0.2

while(feed_descriptor.isOpened()):
    # Read frame by frame
    current_frame = feed_descriptor.read()[1]
    # if current_frame has a value, transform it to grayscale and blur the frame
    if current_frame is not None:
        gray_current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        smooth_current_frame = cv2.GaussianBlur(gray_current_frame, (9, 9), 0)

        if running_avg is None:
            # If this is the first frame, set running_avg to current frame
            running_avg = np.float32(smooth_current_frame[250:400, 300:400])
            running_avg2 = np.float32(smooth_current_frame[250:400, 500:600])

        else:
            # diff_frame is the absolute difference between the current frame and the running weighted average of previous frames
            diff_frame = cv2.absdiff(np.float32((smooth_current_frame[250:400, 300:400])), np.float32((running_avg)))
            diff_frame2 = cv2.absdiff(np.float32((smooth_current_frame[250:400, 500:600])), np.float32((running_avg2)))
            # accumulateWeighted averages the current frame along with the previous frames in a weighted manner
            cv2.accumulateWeighted(np.float32(smooth_current_frame[250:400, 300:400]), running_avg, alpha)
            cv2.accumulateWeighted(np.float32(smooth_current_frame[250:400, 500:600]), running_avg2, alpha)
            # threshold function will transfrom the pixel to white if the difference is above motion_thresh value,
            # it will transorm the pixel to black if it is below the threshold
            _, subtracted = cv2.threshold(diff_frame, motion_thresh, 1, cv2.THRESH_BINARY)
            _, subtracted2 = cv2.threshold(diff_frame2, motion_thresh, 1, cv2.THRESH_BINARY)
            # motion_fraction is the percentage of pixels on the entire framethat are moving
            motion_fraction = (sum(sum(subtracted))/(subtracted.shape[0]*subtracted.shape[1]))
            # Adds each motion fraction to a list called motion_fractions
            motion_fractions.append(motion_fraction)
            motion_fraction2 = (sum(sum(subtracted2)) / (subtracted2.shape[0] * subtracted2.shape[1]))
            motion_fractions2.append(motion_fraction2)

    # Check if current frame is not different from NONE
    elif current_frame is None:
        break

# commented out print statements to check values of different lists in the process
#print(diff_frame)
#print(motion_fractions)
#print(len(motion_fractions))
#print(diff_frame2)
#print(motion_fractions2)
#print(len(motion_fractions2))

# plot the % of pixels that change for both ROIs
plt.plot(np.array(motion_fractions), 'b')
plt.plot(np.array(motion_fractions2),'r')
plt.ylabel('Number of pixels that change')
plt.axis([0,60,0,0.9])
plt.show()


