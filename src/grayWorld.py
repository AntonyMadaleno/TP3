# Import necessary libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Gray World
def grayWorld(rgb_input):

    #create the rgb_corrected matrix
    rgb_corrected = np.zeros(rgb_input.shape, dtype= np.uint8)

    #mean values of R,G and B
    avg_R = np.mean(rgb_input[:,:,0].astype(float))
    avg_G = np.mean(rgb_input[:,:,1].astype(float))
    avg_B = np.mean(rgb_input[:,:,2].astype(float))

    #average intensity across all channel
    average = (avg_R + avg_G + avg_B) / 3

    # Perform the gray world correction and use np.clip to limit values to [0, 255]
    rgb_corrected[:, :, 0] = np.clip((average / avg_R) * rgb_input[:, :, 0], 0, 255)
    rgb_corrected[:, :, 1] = np.clip((average / avg_G) * rgb_input[:, :, 1], 0, 255)
    rgb_corrected[:, :, 2] = np.clip((average / avg_B) * rgb_input[:, :, 2], 0, 255)

    return rgb_corrected