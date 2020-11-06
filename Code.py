# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import cv2 as cv
import numpy as np
from skimage import data
from skimage.feature import match_template
import random
# load image as pixel array
groupImage = cv.imread('groupGray.jpg')
targetImage = cv.imread('boothiGray.jpg')

#defining all the required functions or functionality HERE
def DecToBin(n):
    a=[]
    while(n>0):
        dig=n%2
        a.append(dig)
        n=n//2
    a.reverse()
    if len(a) == 0:
        a.append(0)
    return a
def BinToDec(binNum):
    # print(binNum)
    res = int("".join(str(x) for x in binNum), 2)
    return res 
#In the image variable,  we have an ndarray contain the pixels of group image
#512 rows, 1024 colums 
populationList = []
populationSize = 100
matchPoints = []
corellatedValues = {}


#initializing Population with randomly generated points or co-ordinates
def initializePopulationRandomly():
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


# CheckOut Corelations

def CheckForCoRelation(threashold):
    for po in range(0, populationSize):

        x1 = populationList[po][0]
        y1 = populationList[po][1]

        colsInSmallImage = len(targetImage[0]) # 29 colums
        rowsInSmallImage = len(targetImage)    # 35 Rows 

        x2 = x1 + rowsInSmallImage
        y2 = y1 + colsInSmallImage
        if (x2 < 512) and (y2 < 1024):
            co_related_value = 0
            croppedIMG = groupImage[ x1:x2, y1:y2]
            co_related_value = match_template(targetImage, croppedIMG)

            # co_related_value = ( co_related_value / (23*35) ) * 100
            
            #print(co_related_value) 

            corellatedValues[x1, y1] = [co_related_value[0][0][0]]

            if co_related_value >= threashold:
                matchPoints.append([x1,y1])
        else:
            corellatedValues[x1,y1] = [0]        
    if len(matchPoints) == 0:
        return False
    else:
        return True    

# SORTING THE DICTIONARY According To The Keys // Also Checking for fitness
#Keys -- a points having a value of corelation
def CheckForFitness(unsortedCoRelatedValues):
    sortedPopulationList = []
    corellatedValuesSortedList = sorted(unsortedCoRelatedValues.items(), key=lambda x: x[1])
    # print(corellatedValuesSortedList[0])
    newDict = dict(corellatedValuesSortedList)
    i = 0
    for key in newDict.keys():
        # if i == 0:
        #     print(newDict[key])
        #     i+=1
        sortedPopulationList.append(key)
    return sortedPopulationList

# Crossover and mutating the values in populationList and refilling the populationList
def CrossoverAndMutate(sortedPopulationList):
    populationList.clear()
    for i in range(0, len(sortedPopulationList)-1, 2):
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
        # print(f"Before Crossover: p1: {p1} \n p2: {p2}")
        p1.reverse()
        p2.reverse()
        for i in range(0, rand):
            p1[i], p2[i] = p2[i], p1[i]
        p1.reverse()
        p2.reverse()
        # print(f"after crossover {rand} \n, p1: {p1} \np2: {p2}")
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
        newP1_x = []
        newP1_y = []
        newP2_x = []
        newP2_y = []
        for i in range(0, len(pt1Bin)):
            newP1_x.append(p1.pop())
        newP1_y = p1
        for i in range(0, len(pt3Bin)):
            newP2_x.append(p2.pop())
        newP2_y = p2
        # print(newP1_x, newP1_y)
        # print(newP2_x, newP2_y)
        x1 = BinToDec(newP1_x)
        y1 = BinToDec(newP1_y)

        x2 = BinToDec(newP2_x)
        y2 = BinToDec(newP2_y)
        temp1 = [x1, y1]
        temp2 = [x2, y2]
        populationList.append(temp1)
        populationList.append(temp2)

def main():
    threashold = 0.9
    termVar = 1000
    initializePopulationRandomly()
    while (termVar > 0):
        if CheckForCoRelation(threashold):
            print("Match Found ....{}" .format(matchPoints))
            break
        sortedFitness = CheckForFitness(corellatedValues)
        CrossoverAndMutate(sortedFitness)
        termVar -= 1



if __name__== "__main__":
    main()
    print("booooom")












