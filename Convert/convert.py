from PIL import Image
import matplotlib.pylab as plt
import numpy as np 

def picTo01(filename):
    img=Image.open(filename).convert('RGBA')

    raw_data=img.load()
#Noise reduction and resize to 32*32
    for y in range(img.size[1]):
       for x in range(img.size[0]):
           if raw_data[x,y][0]<90:
               raw_data[x,y]=(0,0,0,255)

 
    for y in range(img.size[1]):
       for x in range(img.size[0]):
           if raw_data[x,y][1]<136:
               raw_data[x,y]=(0,0,0,255)


    for y in range(img.size[1]):
       for x in range(img.size[0]):
           if raw_data[x,y][2]>0:
               raw_data[x,y]=(255,255,255,255)


    img=img.resize((32,32),Image.LANCZOS)

    img.save('test'+filename.split('.')[0]+'.png')

    array=plt.array(img)

    gray_array=np.zeros((32,32))

    for x in range(array.shape[0]):
       for y in range(array.shape[1]):
           gray=0.299*array[x][y][0]+0.587 * array[x][y][1] + 0.114 * array[x][y][2]
           #white
           if gray==255:
               gray_array[x][y]=0
            #black
           else:
                gray_array[x][y]=1
    #NAME
    name01=filename.split('.')[0]
    name01=name01+'.txt'


    np.savetxt(name01,gray_array,fmt='%d',delimiter='')


picTo01('2.PNG')




    






