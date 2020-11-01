# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import cv2 as cv
import numpy as np
import random
# load image as pixel array
groupImage = cv.imread('groupGray.jpg')
targetImage = cv.imread('boothiGray.jpg')

#In the image variable,  we have an ndarray contain the pixels of group image
#512 rows, 1024 colums 

############################################
#    STEP NO 1 

# Generate random populations in term of (x,y)

populationList = []
populationSize = 100

for i in range(populationSize):
    x = random.randint(0, 512)
    y = random.randint(0, 1024)
    if (x+len(targetImage)) > len(groupImage) or (y+len(targetImage[0])) > len(groupImage[0]):
        i = i - 1
    else:
        populationList.append([x,y])

#  Initial Population Is Generated

############################################


# STEP NO 2 

# CheckOut Corelations



for pop in range(0, populationSize):
    matchPercentage = 0
    x1 = populationList[pop][0]
    y1 = populationList[pop][1]

    colsInSmallImage = len(targetImage[0]) # 29 colums
    rowsInSmallImage = len(targetImage)    # 35 Rows 

    x2 = x1 + rowsInSmallImage
    y2 = y1 + colsInSmallImage


    

    for row in range(len(targetImage)):
        for col in range(len(targetImage[0])):
            if groupImage[x1+row][y1+col][0] == targetImage[row][col][0] and groupImage[x1+row][y1+col][0] == targetImage[row][col][0]:
                matchPercentage+=1
            print("Match Found : " + str(matchPercentage))
            




#with open("newfile.txt", "w") as fileh:
 #   for row in image:
  #      fileh.write("\n%s"%row)

