git地址:https://github.com/koukoulala/SN_essay.git
都是用DNN做的，迭代2000次
1.facebook数据集：
只看直接相邻的邻居数目的表：18列特征，18个类别，准确度0.98
只有第2种邻居结构的表：18列特征，18个类别，准确度0.90
只有第3种邻居结构的表：18列特征，18个类别，准确度0.89
3种邻居结构的表（第一列是全部邻居数目）：54列特征，18个类别，准确度0.972
2.bcspwr数据集：
只看直接相邻的邻居数目的表：8列特征，8个类别，准确度0.8377
只有第2种邻居结构的表：8列特征，8个类别，准确度0.6396
只有第3种邻居结构的表：8列特征，8个类别，准确度0.2415
3种邻居结构的表（第一列是全部邻居数目）：24列特征，8个类别，准确度0.8415
指定3种结构的影响度，直接测试准确率：都设置为1，准确度0.824；设置为（1,0,0）即只有直接相邻节点起作用的话，准确度0.821
使用cnn，把每个节点邻居结构看做是图，并且数目都*10（为了防止梯度消失），准确率0.8359
3.fpga数据集：
只看直接相邻的邻居数目的表：16列特征，16个类别，准确度0.9918
3种邻居结构的表（第一列是全部邻居数目）：48列特征，16个类别，准确度0.9918