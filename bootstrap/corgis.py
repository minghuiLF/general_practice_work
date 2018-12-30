import numpy as np
import random
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pprint import pprint


def calcSampleVariance(data):
	sampleMean = np.mean(data)
	n = len(data)
	total = 0
	for i in range(n):
		d = data[i]
		total += math.pow(d - sampleMean, 2)
	return float(total)/ (n-1)

def plotHistogram(x,ax=None ,block = True):
	n, bins, patches = ax.hist(x,np.arange(0,10,0.1), edgecolor="black",facecolor='green', alpha=0.75)
	ax.set_xlabel('Value')
	ax.set_ylabel('Count')
	ax.grid(True)
	ax.set_title('Data Histogram')
	# plt.show(block)


pop1=[13, 12, 7, 16, 9, 11, 7, 10, 9, 8, 9, 7, 16, 7, 9, 8, 13, 10, 11, 9, 13, 13, 10, 10, 9, 7, 7, 6, 7, 8,12, 13, 9, 6, 9, 11, 10, 8, 12, 10, 9, 10, 8, 14, 13, 13, 10, 11, 12, 9]

pop2=[8, 8, 16, 16, 9, 13, 14, 13, 10, 12, 10, 6, 14, 8, 13, 14, 7, 13, 7, 8, 4, 11, 7, 12, 8, 9, 12, 8, 11,10, 12, 6, 10, 15, 11, 12, 3, 8, 11, 10, 10, 8, 12, 8, 11, 6, 7, 10, 8, 5]



pop1=np.array(pop1)
pop2=np.array(pop2)
n=len(pop1)
m=len(pop2)
print(n,m)
diff=9.0-6.0

unipop=np.append(pop1, pop2)
# for i in range(50):
#     print(pop1[i])
#     print(unipop[i])
# for i in range(50):
#     print(pop2[i])
#     print(unipop[i+50])


count=0
count2=0
dd=np.array([])
dd2=np.array([])
for  i in range(10000):
    sub_sample1=np.random.choice(unipop,n)
    sub_sample2=np.random.choice(unipop,n)

    sub_sam1=random.sample(list(unipop),m)
    sub_sam2=random.sample(list(unipop),m)
    ## two sample way(functions) give a very different answer


    sub_sample_variance1 =n/(n-1)*np.var(sub_sample1)

    sub_sample_variance2 =m/(m-1)*np.var(sub_sample2)

    sub_sample_varia1 =n/(n-1)*np.var(sub_sam1)

    sub_sample_varia2 =m/(m-1)*np.var(sub_sam2)

    # print(sub_sample_variance1,sub_sample_variance2)
    Dd=abs(sub_sample_variance1-sub_sample_variance2)
    Dd2=abs(sub_sample_varia1-sub_sample_varia2)

    dd=np.append(dd,Dd)
    dd2=np.append(dd2,Dd2)
    if  diff <= Dd:
        count+=1

    if  diff <= Dd2:
        count2+=1

print (float(count)/10000)
print (float(count2)/10000)
# print(dd)
fi=plt.figure()

ax1=fi.add_subplot(121)
ax2=fi.add_subplot(122)

plotHistogram(dd,ax=ax1)
plotHistogram(dd2,ax=ax2)

plt.show()

# a=random.sample(list(unipop),n)
# print(calcSampleVariance(a))
# print(n/(n-1)*np.var(a))
