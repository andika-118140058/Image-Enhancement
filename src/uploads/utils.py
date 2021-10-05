import cv2
import numpy as np

def negative(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    y, x = image.shape
    negative = np.zeros( (y,x), dtype="uint8" )
    for i in range(y):
        for j in range(x):
            negative[i,j] = 255 - image[i,j]
    negative=negative.astype("uint8")
    return negative

def get_filtered_image(image, action):
    # img = cv2.cvtColor(image, cv2.COLOR)
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'GREYSCALE':
        filtered = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # filtered = cv2.imread("irene.jpg",cv2.IMREAD_GRAYSCALE)
    elif action == 'NEGATIVE':
        filtered = negative(image)
    elif action == 'BRIGHTENING':
        pass
    else:
        pass

    return filtered