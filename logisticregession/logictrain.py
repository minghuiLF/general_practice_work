import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def sigmod(sitas,xs):
    sitas=np.array(sitas)
    xs=np.array(xs)
    # print(sitas,xs,-1*np.sum(sitas+xs))
    stx=(-1)*np.sum(sitas*xs)
    return 1/(1+np.exp(stx))


def genarate_data(size=200,t=2):
    a=np.arange(-20,20,0.2)

    a=a.reshape((size,1))
    a=a.repeat(3,1)
    b=a.copy()
    dv=np.random.randint(20,size=(size))
    a[:,2]=1
    a[:,1]*=t
    a[:,1]+=dv
    b[:,2]=0
    b[:,1]*=t
    b[:,1]-=dv
    data=np.concatenate((a,b))
    sita0=np.ones((size*2,1))
    return np.concatenate((sita0,data),axis=1)
    plt.scatter(a[:,0], a[:,1],color='r')
    plt.scatter(b[:,0], b[:,1],color='b')
    plt.show()








data=genarate_data()

# data=[[1,0,1,1],
#       [1,1,1,1],
#       [1,1,0,1]
#      ]

print(data)
print("----------")
Features=2
U=0.00001


sitas=[0]*(Features+1)

c=0
while c<5000:
    gradient=[0]*(Features+1)
    # print(gradient)
    # print("----------gradient!!1")
    for dt in data:
        x,y=dt[:-1],dt[-1]
        SS=sigmod(sitas, x)
        for j in range(Features+1):
            gradient[j]+=(y-SS)*x[j]

    print(gradient)
    print("----------gradient")

    for i in range(Features+1):
        sitas[i]+=U*gradient[i]
    print(sitas)
    print("----------sitas")
    if np.sum(gradient)<0.03 and np.sum(gradient)>-0.03:
        print("<0.3")
        break
    c+=1





plt.scatter(data[200:,1], data[200:,2],color='r', alpha=0.5)
plt.scatter(data[:200,1], data[:200,2],color='b', alpha=0.5)

T_data=genarate_data(size=200,t=1)

for dd in T_data:
    p=sigmod(sitas, dd[:-1])

    if p>0.5:
        plt.scatter(dd[1], dd[2],color='green',alpha=0.5)
    else:
        plt.scatter(dd[1], dd[2],color='yellow',alpha=0.5)



plt.show()
