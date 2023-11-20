import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Patch Blanc
def patchBlanc(rgb_input):

    #create the rgb_corrected matrix
    rgb_corrected = np.zeros(rgb_input.shape, dtype= np.uint8)

    #max values of R,G and B
    max_R = np.max(rgb_input[:,:,0].astype(float))
    max_G = np.max(rgb_input[:,:,1].astype(float))
    max_B = np.max(rgb_input[:,:,2].astype(float))

    # Perform the gray world correction and use np.clip to limit values to [0, 255]
    rgb_corrected[:, :, 0] = np.clip((255 / max_R) * rgb_input[:, :, 0], 0, 255)
    rgb_corrected[:, :, 1] = np.clip((255 / max_G) * rgb_input[:, :, 1], 0, 255)
    rgb_corrected[:, :, 2] = np.clip((255 / max_B) * rgb_input[:, :, 2], 0, 255)

    return rgb_corrected

def patchBlancModifie(rgb_input,seuil):

    #create the rgb_corrected matrix
    rgb_corrected = np.zeros(rgb_input.shape, dtype= np.uint8)

    #get all value above threshold
    Rh = (rgb_input[:,:,0]>seuil).astype(float)
    Gh = (rgb_input[:,:,1]>seuil).astype(float)
    Bh = (rgb_input[:,:,2]>seuil).astype(float)

    #number of values above threshold
    nR = np.sum(Rh)
    nG = np.sum(Gh)
    nB = np.sum(Bh)

    #Average of values above threshold
    avg_R = np.sum( Rh * rgb_input[:,:,0].astype(float) ) / nR if nR != 0 else 1
    avg_G = np.sum( Gh * rgb_input[:,:,1].astype(float) ) / nG if nG != 0 else 1
    avg_B = np.sum( Bh * rgb_input[:,:,2].astype(float) ) / nB if nB != 0 else 1

    # Perform the gray world correction and use np.clip to limit values to [0, 255]
    rgb_corrected[:, :, 0] = np.clip((255 / avg_R) * rgb_input[:, :, 0], 0, 255) if nR != 0 else rgb_input[:, :, 0]
    rgb_corrected[:, :, 1] = np.clip((255 / avg_G) * rgb_input[:, :, 1], 0, 255) if nR != 1 else rgb_input[:, :, 1]
    rgb_corrected[:, :, 2] = np.clip((255 / avg_B) * rgb_input[:, :, 2], 0, 255) if nR != 2 else rgb_input[:, :, 2]

    return rgb_corrected