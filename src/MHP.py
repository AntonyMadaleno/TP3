from grayWorld import *
from whitePatch import *
import numpy as np

def MHP(img_in, low, high):

    #intensity
    gray = ( img_in[:,:,0].astype(float) + img_in[:,:,1].astype(float) + img_in[:,:,2].astype(float) ) / 3.0

    #calcul delta (gradient entre patch blanc / monde gris)
    delta = np.clip(1 / (high - low) * gray - low / (high - low), 0.0, 1.0)

    gworld = grayWorld(img_in) * (1 - delta)[:,:,np.newaxis]
    pblanc = patchBlanc(img_in) * delta[:,:,np.newaxis]

    return (gworld + pblanc).astype(np.uint8)