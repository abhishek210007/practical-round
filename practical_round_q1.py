def missingRpt(n,L):
    N = n.sort()
    
    U_list=[]
    R_list=[]
    miss=[]
    for i in (n):
        if i not in U_list:
            U_list.append(i)
        elif i not in R_list:
            R_list.append(i)
    for j in range(1,L):
        if j not in n:
            miss.append(j)
    return R_list,miss  #returning 1)repeated value 2)missing value. 

a=[1,2,4,4]
x= missingRpt(a,4)
print(x)
