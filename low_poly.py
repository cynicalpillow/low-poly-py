#Pre-process the input image to remove noise and reduce image size
#Detect edges in the input image
#If the image contains humans faces, detect facial features as well
#Choose a random subset of the above detected points / edges
#Triangulate using Delaunay Triangulation
#Fill the triangles with the mean value of all pixels contained by it (in parallel for faster computation)

import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

def show_images(imgs, rows, columns):
    l = len(imgs)
    for i, img in enumerate(imgs):
        plt.subplot(rows, columns, i+1), plt.imshow(img)
    plt.show()

def reduce_image_size():
    pass

def noise_reduction(img):
    return cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

def edge_detection():
    pass

def facial_detection():
    pass

def triangulation():
    pass

def fill_in_pixels():
    pass

def get_image(image_name):
    return cv2.imread(image_name)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Invalid arguments")
        exit(0)

    img = get_image(sys.argv[1])
    dst = noise_reduction(img)
    show_images([img, dst], 2, 1)
