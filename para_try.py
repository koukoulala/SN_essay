import tensorflow as tf
import numpy as np
from numpy import *

#整理一下csv文件，将cnn中得到的3个权重在整个数据集上测试准确率，并将分类出错的情况保存在csv中
def test_para(filepath,w,n):
    #参数：文件位置，3种结构影响度构成的列表，图中类别数目，acc是准确率，err是分类错误的个数，fal是错误的行数
    acc=0;err=0;fal=[]
    data_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=filepath,
        target_dtype=np.int,
        features_dtype=np.int)

    #data是所有数据，true_label是节点真实类别，pre_labels是预测类别，Y是每个节点每种类别的可能性，其中最大可能的类别放入pre_labels
    data=data_set.data
    true_labels=data_set.target
    pre_labels=np.zeros(len(data),int)
    Y=np.zeros([len(data),n],int)
    #ma是一行中最大的数,k代表ma的index，j代表类别
    for i in range(0,len(data)):
        ma=-100000;k=0
        for j in range(n):
            num=data[i][j*3]*w[0]+data[i][j*3+1]*w[1]+data[i][j*3+2]*w[2]
            Y[i][j]=num
            if num>ma:
                ma=num
                k=j
        #print(Y[i]," ",k)
        pre_labels[i]=k
        if pre_labels[i] != true_labels[i]:
            err+=1
            wrong=[i,true_labels[i],pre_labels[i]]    #记录下第几行被分错，真实类别与被预测的类别
            fal.append(wrong)
    print("错误的总数目：",err)
    acc=1-(err/len(data))
    savetxt("tmp/para_try.csv", fal, fmt="%d", delimiter=",")
    return acc

if __name__ == "__main__":
    acc=test_para("tmp/bcspwr_node_test.csv",[0.86749744,1.0554432,0.38650352],8)
    print("准确率为：",acc)