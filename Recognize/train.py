import os.path
import numpy as np
#convert 32*32 to 1*1024
def img32to1024(filename):
    returnVect=np.zeros((1,1024))
    fr=open(filename,'r')
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

#collect train to a matrix and identify class
hwLabels=[]
trainingFileList=os.listdir('trainingDigits')
m=len(trainingFileList)
trainingMat=np.zeros((m,1024))
for i in range(m):
    fileNameStr=trainingFileList[i]
    fileStr=fileNameStr.split('.')[0]
    classNumStr=int(fileStr.split('_')[0])
    hwLabels.append(classNumStr)
    trainingMat[i,:]=img32to1024('trainingDigits/%s' % fileNameStr)








