from find_structure import *
save_csv=[]
kernal_val=[[[[-0.00488317]],[[-0.00656881]],[[ 0.00183626]]]]
print(kernal_val[0][0][0])
print(kernal_val[0][1][0])
print(kernal_val[0][2][0])
tmpL=[1,2]
tmpL.append(kernal_val[0][1][0][0])
save_csv.append(tmpL)
tmpL=[]
tmpL.append(2)
tmpL.append(2)
tmpL.append(kernal_val[0][0][0][0])
save_csv.append(tmpL)
print(save_csv)

savetxt("save_csv.csv",save_csv,fmt="%f",delimiter=",")