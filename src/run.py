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

i = 0
for tuple in tuple_list:

    print('current image : ' + tuple[0] + "\n")

    img = cv2.imread("../Images_TP3/Test1/" + tuple[0] + "." + tuple[2])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_orig = cv2.imread("../Images_TP3/Test1/" + tuple[1] + "." + tuple[2])
    img_orig = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

    img_grayWorld = grayWorld(img)
    img_patchBlanc = patchBlanc(img)
    img_MHP = MHP(img, 80, 220)
    img_patchBlancModif = patchBlancModifie(img, 200)

    fig = plt.figure(figsize = (12,7))
    columns = 3
    rows = 2

    fig.add_subplot(rows, columns, 1)
    plt.imshow(img, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('original')

    fig.add_subplot(rows, columns, 2)
    plt.imshow(img_orig, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('Truth')

    fig.add_subplot(rows, columns, 3)
    plt.imshow(img_grayWorld, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('grayWorld')

    fig.add_subplot(rows, columns, 4)
    plt.imshow(img_patchBlanc, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('patchBlanc')

    fig.add_subplot(rows, columns, 5)
    plt.imshow(img_patchBlancModif, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('patchBlancModif')

    fig.add_subplot(rows, columns, 6)
    plt.imshow(img_MHP, cmap='Greys_r', interpolation='nearest')
    plt.axis('off')
    plt.title('MHP')
    plt.savefig("../result/figures/figure_" + tuple[0] + ".png")
    i = i+1