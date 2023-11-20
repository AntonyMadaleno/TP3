import numpy as np
import cv2

# Define a function to calculate Mean Squared Error (MSE) between two images
def MSE(i1, i2):
    return np.mean((i1 - i2)**2)

# Define a function to calculate local MSE
def MSE_local(i1, i2, bsize=16):
    x_block_count = i1.shape[1] // bsize
    y_block_count = i1.shape[0] // bsize

    mse_map = np.zeros((y_block_count, x_block_count))
    
    for y in range(0, y_block_count):
        for x in range(0, x_block_count):
            bs_x = x * bsize
            bs_y = y * bsize
            be_x = bs_x + bsize
            be_y = bs_y + bsize

            mse_map[y, x] = MSE(i1[bs_y:be_y, bs_x:be_x], i2[bs_y:be_y, bs_x:be_x])
    
    return mse_map

def delta_E(i1, i2):

    i1_lab = cv2.cvtColor(i1, cv2.COLOR_RGB2Lab)
    i2_lab = cv2.cvtColor(i2, cv2.COLOR_RGB2Lab)

    dE = (i1_lab - i2_lab)**2
    dE = dE[:,:,0] + dE[:,:,1] + dE[:,:,2]
    dE = np.sqrt(dE)

    return dE

def delta_E_mean(i1, i2):
    return np.mean(delta_E(i1,i2))