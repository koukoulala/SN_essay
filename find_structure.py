from numpy import *

#寻找那10%的节点的邻居节点结构，以一个节点为例子，153来测试，度数最大
# 其communite=3(并且为了有w4的结构，手动加了（35,33）边）

#读取边表文件和communite放入list中
def read_file(Lfile,Cfile):
    L=[];LL=set();C={};
    with open(Lfile,'r')as f:
        for line in f.readlines():
            line=[int(x) for x in line.split()]
            L.append(line)
            for i in line:
                LL.add(i)
    with open(Cfile,'r')as f:
        for line in f:
            (key,value)=[int(x) for x in line.split()]
            C[key]=value
    return L,C,LL

#分别获得三种结构的个数,得到n行3列的二维数组，W[i][j]=k代表Communite=i的节点的wj结构有k个
def find_stru(L,n,C,Tnode):
    #新建一个n行4列的零矩阵
    W=zeros([n,3],int16)

    #新建一个内嵌列表，维数为n，每个内部列表长度未知,l=[[],[],[],[],[]]
    l=[];i=0;
    while i!=n:
        l.append([])
        i+=1
    for i in L:
        if i[1] == Tnode:
        # 把直接前驱点记录在不同的communite里面
            l[C[i[0]]].append(i[0])
    #print("目标节点",Tnode,"的直接前驱情况:",l)

    #一个类别一个类别的来计算不同结构数目，存储在W中,W[k][0]中是邻居节点的总个数
    k=0
    for ll in l:
        if ll!=[]:
            W[k][0]=len(ll)
            for i in ll:
                flag=0; #如果flag=0，也就是不存在w2结构
                for j in L:
                    if j[1]==i and C[j[0]]==k: # 前驱点有前驱,且类别也相同
                        flag = 1;
                        k2 = j[0]
                        if k2 in ll:  # 前驱的前驱也是直接前驱，w3的结构
                            W[k][2] += 1;
                        else:
                            W[k][1] += 1;
                #if flag == 0:
                    #W[k][0] += 1;
        k+=1

    #print("目标节点",Tnode,"有",n,"种类别，每个类别3种结构数目:")
    #print(W)
    return W
