import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data=pd.read_csv("peerGrades.csv",header=None)


print(data.values.mean())

means=[]
meidans=[]
for i in range(10000):
    sample=np.random.choice(data[0],size=5)

    m=sample.mean()
    means.append(m)

    medi=np.median(sample)
    meidans.append(medi)
print('mean_var,median_var')
print(np.var(means))
print(np.var(meidans))
print("mean diff")
print(np.mean(means))
print(np.mean(meidans))


plt.hist(means,range(0,101),color='blue',edgecolor='black', alpha=0.5,label='means')

plt.hist(meidans,range(0,101),color='green',edgecolor='black',alpha=0.5,label='medians')

plt.hist(data.values,range(0,101),color='yellow',edgecolor='black',alpha=0.5,label='data')

plt.axvline(x=np.mean(meidans), color = 'r')

plt.legend()

plt.show()
