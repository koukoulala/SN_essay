from find_structure import *

Lfile='data/bcspwr10/bcspwr10.txt';
Cfile='data/bcspwr10/bcspwr10_communities.txt'
L,C,LL=read_file(Lfile,Cfile)

#计算图有几个Communites
n=0;k=[];
for key in C:
    if C[key] not in k:
        k.append(C[key])
        n+=1
print("图的commnunite类型：",k)
print("图的commnunite数目=",n)

#把3邻居结构数目保存到csv文件中
train_node=LL
train_data=zeros([len(train_node),n*3],int)
node_name=zeros(len(train_data),int) #节点名称，放在第一列
label_data=zeros(len(train_data),int)
k=0;
for Trnode in train_node:
    W=find_stru(L,n,C,Trnode)
    W2=W.reshape(n*3,order='C')
    #print("转换成行向量",W2)#一行有n*3列
    train_data[k]=W2
    node_name[k]=Trnode
    label_data[k]=C[Trnode]
    k+=1

train_data=c_[train_data,label_data]
train_data=c_[node_name,train_data]

#读取para_try.csv文件中出错的节点，让对应为正确label的w3列数目都加2，看看最后输出权重值w3会不会比较高
i=0
with open("result/para_try.csv","r") as f:
    for lines in f.readlines():
        line=lines.strip("\n").split(",")
        train_data[int(line[0])][int(line[1])*3+3]+=1;
        i+=1;
        if i==600:
            break;
print(train_data)

savetxt("result/bcspwr_node_trick.csv",train_data,fmt="%d",delimiter=",")
