import os.path
import numpy as np
import train as tr
def classify(inX,k):
    dataSetSize=tr.m
    diffMat=inX-tr.trainingMat
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    #get the rank
    sortedDistances=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=tr.hwLabels[sortedDistances[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),reverse=True)
    return sortedClassCount[0][0]




#test
testFileList=os.listdir('testDigits')
errorCount=0.0
mTest=len(testFileList)
realLabel=[]
testLabel=[]
for i in range(mTest):
    fileNameStr=testFileList[i]
    fileStr=fileNameStr.split('.')[0]
    classNumStr=int(fileStr.split('_')[0])
    vectorUnderTest=tr.img32to1024('testDigits/%s' % fileNameStr)
    testLabel=classify(vectorUnderTest,3)
    print("the classifier came back with:%s, the real answer is:%s" %(testLabel,classNumStr))
    if(testLabel!=classNumStr):
        errorCount+=1.0

print(errorCount/mTest)
