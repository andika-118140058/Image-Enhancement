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

def brightening(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    y, x = image.shape
    bright = np.zeros( (y,x), dtype="uint8" )
    for i in range(y):
        for j in range(x):
            temp = image[i,j] + 100
            if (temp<0):
                bright[i,j] = 0
            elif (temp>255):
                bright[i,j] = 255
            else:
                bright[i,j] = temp
    bright=bright.astype("uint8")
    return bright

def boolean(image):
    shape = len(image.shape)
    if shape==3:
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    thresh, biner = cv2.threshold(image, 125, 255, cv2.THRESH_BINARY)
    notBooleanImage = cv2.bitwise_not(biner)
    return notBooleanImage

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
        filtered = brightening(image)
    elif action == 'BOOLEAN':
        filtered = boolean(image)
    else:
        pass

    return filtered