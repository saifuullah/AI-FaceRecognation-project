# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import cv2 as cv
import numpy as np
import random
# load image as pixel array
image = cv.imread('groupGray.jpg')
 # summarize shape of the pixel array

#In the image var,  we have an ndarray contain the pixels of group image
#512 rows, 1024 colums 

############################################
#    STEP NO 1 

# Generate random populations in term of (x,y)

populationList = []
populationSize = 100

for i in range(populationSize):
    x = random.randint(0, 512)
    y = random.randint(0, 1024)
    populationList.append([x,y])

#  Initial Population Is Generated

############################################







#with open("newfile.txt", "w") as fileh:
 #   for row in image:
  #      fileh.write("\n%s"%row)
