import numpy as np
import time
import pandas as pd

from grayWorld import *
from whitePatch import *
from MHP import *

def readList(file_path):
    
    tuple_list = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Split each line by a comma and remove leading/trailing whitespace
                names = [name.strip() for name in line.strip().split(',')]

                # Check if there are two names
                tuple_list.append(names)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        # Handle the file not found error here

    return tuple_list

filepath = "../Images_TP3/ListTest1.txt"
tuple_list = readList(filepath)

Methods = ["Gray World", "White Patch", "White Patch w Threshold", "MHP"]

i = 0
for tuple in tuple_list:

    print('current image : ' + tuple[0] + "\n")
    result = np.zeros((5,2), dtype = float)
    img = cv2.imread("../Images_TP3/Test1/" + tuple[0] + "." + tuple[2])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    I0 = time.time()
    img_grayWorld = grayWorld(img)
    I1 = time.time()
    img_patchBlanc = patchBlanc(img)
    I2 = time.time()
    img_MHP = MHP(img, 80, 220)
    I3 = time.time()
    img_patchBlancModif = patchBlancModifie(img, 200)
    I4 = time.time()

    exec_times = [(I1 - I0) * 1e3, (I2 - I1) * 1e3, (I3 - I2) * 1e3, (I4 - I3) * 1e3]
    rows, columns = result.shape

    # Create a DataFrame
    df = pd.DataFrame(exec_times, columns=['time_ms'])

    # Save the DataFrame to a CSV file
    csv_file_path = '../result/csv/time_evaluation/statistics_' + tuple[0] + '.csv'  # Replace with your desired file path
    df.index = list(Methods)
    df.to_csv(csv_file_path, index=True)

    i = i + 1
