import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data = pd.read_csv("learningOutcomes.csv",header=None)

act1=(data.loc[data[1]=="activity1"])[2]
act2=(data.loc[data[1]=="activity2"])[2]



# print(act1.mean(),act2.mean())

diff=abs(act1.mean()-act2.mean())

# print(diff)

count=0
for i in range(10000):
    sub_sample1=np.random.choice(data[2],len(act1))
    sub_sample2=np.random.choice(data[2],len(act2))

    n=abs(sub_sample1.mean()-sub_sample2.mean())
    if n >= diff :
        # print(n)
        count+=1


print(float(count)/10000)


backg=pd.read_csv("background.csv",header=None)

merge=pd.merge(data,backg,on=0)





merge=merge.set_index('1_y')

l=merge.loc['more']
m=merge.loc['average']
s=merge.loc['less']


for group in (l,m,s):
    act1=(group.loc[group['1_x']=="activity1"])[2]
    act2=(group.loc[group['1_x']=="activity2"])[2]



    # print(act1.mean(),act2.mean())

    diff=abs(act1.mean()-act2.mean())

    print("diff:",diff)

    count=0
    for i in range(50000):
        sub_sample1=np.random.choice(group[2],len(act1))
        sub_sample2=np.random.choice(group[2],len(act2))

        n=abs(sub_sample1.mean()-sub_sample2.mean())
        if n >= diff :
            # print(n)
            count+=1

    print("count:",count)
    print(float(count)/50000)
