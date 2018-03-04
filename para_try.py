import tensorflow as tf
import numpy as np

def test_para(filepath,w,n):
    #参数：文件位置，3种结构影响度构成的列表，图中类别数目，acc是准确率，err是分类错误的个数，fal是错误的行数
    acc=0;err=0;fal=[]
    data_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename=filepath,
        target_dtype=np.int,
        features_dtype=np.int)

    #features是特征列，true_label是节点真实类别，pre_labels是预测类别，Y是每个节点每种类别的可能性，其中最大可能的类别放入pre_labels
    features=data_set.data
    true_labels=data_set.target
    pre_labels=np.zeros(len(features),int)
    Y=np.zeros([len(features),n],int)
    #ma是一行中最大的数,k代表ma的index，j代表类别
    for i in range(0,len(features)):
        ma=-100000;k=0
        for j in range(n):
            num=features[i][j*3]*w[0]+features[i][j*3+1]*w[1]+features[i][j*3+2]*w[2]
            Y[i][j]=num
            if num>ma:
                ma=num
                k=j
        print(Y[i]," ",k)
        pre_labels[i]=k
        if pre_labels[i] != true_labels[i]:
            err+=1
            fal.append(i)
    print("错误的总数目：",err)
    print("错误的列分别是：",fal)
    print("被错误的预测为：",list(pre_labels))
    acc=1-(err/len(features))
    return acc

if __name__ == "__main__":
    acc=test_para("tmp/bcspwr/test.csv",[1,0,0],8)
    print("准确率为：",acc)