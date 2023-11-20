import pandas as pd

from grayWorld import *
from whitePatch import *
from MHP import *
from stats import *

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

Methods = ["None", "Gray World", "White Patch", "White Patch w Threshold", "MHP"]

i = 0
for tuple in tuple_list:

    print('current image : ' + tuple[0] + "\n")
    result = np.zeros((5,2), dtype = float)
    img = cv2.imread("../Images_TP3/Test1/" + tuple[0] + "." + tuple[2])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_orig = cv2.imread("../Images_TP3/Test1/" + tuple[1] + "." + tuple[2])
    img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

    img_grayWorld = grayWorld(img)
    img_patchBlanc = patchBlanc(img)
    img_MHP = MHP(img, 80, 220)
    img_patchBlancModif = patchBlancModifie(img, 200)

    result[0,0] = MSE(img_orig, img)
    result[1,0] = MSE(img_orig, img_grayWorld)
    result[2,0] = MSE(img_orig, img_patchBlanc)
    result[3,0] = MSE(img_orig, img_patchBlancModif)
    result[4,0] = MSE(img_orig, img_MHP)

    result[0,1] = delta_E_mean(img_orig, img)
    result[1,1] = delta_E_mean(img_orig, img_grayWorld)
    result[2,1] = delta_E_mean(img_orig, img_patchBlanc)
    result[3,1] = delta_E_mean(img_orig, img_patchBlancModif)
    result[4,1] = delta_E_mean(img_orig, img_MHP)

    rows, columns = result.shape

    # Create a DataFrame
    df = pd.DataFrame(result, columns=['MSE', 'Delta E_Lab'])

    # Save the DataFrame to a CSV file
    csv_file_path = '../result/csv/quality_evaluation/statistics_' + tuple[0] + '.csv'  # Replace with your desired file path
    df.index = list(Methods)
    df.to_csv(csv_file_path, index=True)

    i = i + 1
