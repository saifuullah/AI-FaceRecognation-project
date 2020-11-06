import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from skimage import data
from skimage.feature import match_template


image = cv.imread('groupGray.jpg')
coin = cv.imread('boothiGray.jpg')

result = match_template(coin, coin)
print(result[0][0][0])