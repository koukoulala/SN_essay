from find_structure import *
from sklearn.cross_validation import train_test_split

Lfile='data/fpga_dcop1220/fpga_dcop1220.txt';
Cfile='data/fpga_dcop1220/fpga_dcop1220_communities.txt'
L,C,LL=read_file(Lfile,Cfile)
#print("所有的节点，已去重:")
#print(LL)

#计算图有几个Communites
n=0;k=[];
for key in C:
    if C[key] not in k:
        k.append(C[key])
        n+=1
print("图的commnunite类型：",k)
print("图的commnunite数目=",n)

#把3种邻居结构分别保存到3个csv文件中，把总的保存到第四个
train_node=LL
train_data=zeros([len(train_node),n*3],int)
train_data1=zeros([len(train_node),n],int)
train_data2 = zeros([len(train_node), n], int)
train_data3 = zeros([len(train_node), n], int)
label_data=zeros(len(train_data),int)
k=0;
for Trnode in train_node:
    W=find_stru(L,n,C,Trnode)
    W2=W.reshape(n*3,order='C')
    #print("转换成行向量",W2)#一行有n*3列
    train_data[k]=W2
    train_data1[k]=W[:,0]
    train_data2[k] = W[:, 1]
    train_data3[k]=W[:,2]
    label_data[k]=C[Trnode]
    k+=1

train_data=c_[train_data,label_data]
train_data1 = c_[train_data1, label_data]
train_data2 = c_[train_data2, label_data]
train_data3 = c_[train_data3, label_data]
print(train_data,"\n",train_data1,"\n",train_data2,"\n",train_data3,"\n")

#选取10%的节点作为测试，90%是训练数据节点
trainX,testX=train_test_split(train_data,test_size=0.1,random_state=2)
train1,test1=train_test_split(train_data1,test_size=0.1,random_state=2)
train2,test2=train_test_split(train_data2,test_size=0.1,random_state=2)
train3,test3=train_test_split(train_data3,test_size=0.1,random_state=2)

savetxt("tmp/fpga/train.csv",trainX,fmt="%d",delimiter=",")
savetxt("tmp/fpga/train1.csv", train1, fmt="%d", delimiter=",")
savetxt("tmp/fpga/train2.csv", train2, fmt="%d", delimiter=",")
savetxt("tmp/fpga/train3.csv", train3, fmt="%d", delimiter=",")
savetxt("tmp/fpga/test.csv",testX,fmt="%d",delimiter=",")
savetxt("tmp/fpga/test1.csv", test1, fmt="%d", delimiter=",")
savetxt("tmp/fpga/test2.csv", test2, fmt="%d", delimiter=",")
savetxt("tmp/fpga/test3.csv", test3, fmt="%d", delimiter=",")
