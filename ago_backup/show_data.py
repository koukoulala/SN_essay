import networkx as nx
from operator import itemgetter, attrgetter
import  matplotlib.pyplot as plt

#读取边表文件获得基本信息
def read_file(Gfile):
    G=nx.read_edgelist(Gfile);
    #g=nx.read_edgelist('data/facebook_4039/facebook_4039.txt');
    numNodes=nx.number_of_nodes(G);
    numEdges=nx.number_of_edges(G);
    print('numNodes:',numNodes)
    print("numEdges",numEdges)

    #得到所有节点的度以及图中所有节点的度分布序列（从1至最大度的出现频次）
    #print(G.degree())
    #print(nx.degree_histogram(G))
    #找到度数前10大的节点，用于后面测试
    degree =G.degree()
    degreeSorted = sorted(degree,key=itemgetter(1),reverse=True)
    print("度数最多的前10名",degreeSorted[0:9])

    #nx.draw(G)
    #plt.show()
    #plt.savefig("img/G.png")
    return G;

#给节点添加文本标签
def add_label(G,Gimg):
    f1 = plt.figure()
    nx.draw(G,with_labels=True,font_size=8)
    plt.show()
    f1.savefig(Gimg)

if __name__ == '__main__':
    Gfile='data/facebook_4039/facebook_4039.txt'
    G=read_file(Gfile)
    #add_label(G,'img/G_label.png')
