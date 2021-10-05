import cv2

def get_filtered_image(image, action):
    # img = cv2.cvtColor(image, cv2.COLOR)
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'GREYSCALE':
        filtered = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # filtered = cv2.imread("irene.jpg",cv2.IMREAD_GRAYSCALE)
    elif action == 'NEGATIVE':
        pass
    elif action == 'BRIGHTENING':
        pass
    else:
        pass

    return filtered