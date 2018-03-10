from PIL import Image
import numpy as np
#生成一个数组，维度为100*100，灰度值一定比255大
narray=np.array([range(10000)],dtype='int')
narray=narray.reshape([100,100])
#调用Image库，数组归一化
img=Image.fromarray(narray*255.0/9999)
#转换成灰度图
img=img.convert('L')
#可以调用Image库下的函数了，比如show()
img.show()
#Image类返回矩阵的操作
imgdata=np.matrix(img.getdata(),dtype='float')
imgdata=imgdata.reshape(narray.shape[0],narray.shape[1])
#图像归一化，生成矩阵
nmatrix=imgdata*9999/255.0