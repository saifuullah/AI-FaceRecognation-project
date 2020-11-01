# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import cv2 as cv
import numpy as np
import random
# load image as pixel array
groupImage = cv.imread('groupGray.jpg')
targetImage = cv.imread('boothiGray.jpg')




def DecToBin(n):
    a=[]
    while(n>0):
        dig=n%2
        a.append(dig)
        n=n//2
    a.reverse()
    return a




#In the image variable,  we have an ndarray contain the pixels of group image
#512 rows, 1024 colums 

############################################
#    STEP NO 1 

# Generate random populations in term of (x,y)

populationList = []
populationSize = 100

while(True):
    x = random.randint(0, 512)
    y = random.randint(0, 1024)
    if len(populationList) > 100:
        break
    if (x+len(targetImage)) < len(groupImage) and (y+len(targetImage[0])) < len(groupImage[0]):
        tempList = []
        tempList.append(x)
        tempList.append(y)
        populationList.append(tempList)


#  Initial Population Is Generated

############################################


# STEP NO 2 

# CheckOut Corelations

thresould = 90
matchPoints = []
corellatedValues = { }


for po in range(0, populationSize):
    matchPercentage = 0
   
    x1 = populationList[po][0]
    y1 = populationList[po][1]

    colsInSmallImage = len(targetImage[0]) # 29 colums
    rowsInSmallImage = len(targetImage)    # 35 Rows 

    x2 = x1 + rowsInSmallImage
    y2 = y1 + colsInSmallImage


    

    for row in range(len(targetImage)):    
        for col in range(len(targetImage[0])):
            if groupImage[x1+row][y1+col][0] == targetImage[row][col][0] and groupImage[x1+row][y1+col][1] == targetImage[row][col][1] and groupImage[x1+row][y1+col][2] == targetImage[row][col][2]:
                matchPercentage+=1

    matchPercentage = ( matchPercentage / (len(targetImage)*len(targetImage[0])) ) * 100
    
    #print(matchPercentage) 

    corellatedValues[x1, y1] = [matchPercentage]

    if matchPercentage >= thresould:
        matchPoints.append([x1,y1])
        break            




# STEP NO 3

# SORTING THE DICTIONARY ACCORDING TO THE VALUES

corellatedValuesSortedList = sorted(corellatedValues.items(), key=lambda x: x[1])

newDict = dict(corellatedValuesSortedList)








# STEP NO 4

# CROSS-OVER
binaryDigits = []

sortedPopulationList = []

for key in newDict.keys():
    sortedPopulationList.append(key)

for i in range(0, len(sortedPopulationList), 2):
    pt1 = sortedPopulationList[i][0]
    pt2 = sortedPopulationList[i][1]
    pt3 = sortedPopulationList[i+1][0]
    pt4 = sortedPopulationList[i+1][1]



    pt1Bin = DecToBin(pt1)
    pt2Bin = DecToBin(pt2)
    pt3Bin = DecToBin(pt3)
    pt4Bin = DecToBin(pt4)

    p1 = []
    p2 = []


    for i in pt1Bin:
        p1.append(i)
    for i in pt2Bin:
        p1.append(i)


    for j in pt3Bin:
        p2.append(j)
    for j in pt4Bin:
        p2.append(j)


    l1 = len(p1)
    l2 = len(p2)

    if l1 > l2:
        for i in range(0, (l1-l2)):
            p2.insert(0,0)
    else:
        for i in range(0, (l2-l1)):
            p1.insert(0,0)


    rand = random.randint(0, len(p1)-1)
  

    p1.reverse()
    p2.reverse()

    for i in range(0, rand):
        p1[i], p2[i] = p2[i], p1[i]

    p1.reverse()
    p2.reverse()


# Now Mutation

    rand = random.randint(0, len(p1)-1)
  

    if p1[rand] == 0:
        p1[rand] = 1
    else:
        p1[rand] = 0

    if p2[rand] == 0:
        p2[rand] = 1
    else:
        p2[rand] = 0











