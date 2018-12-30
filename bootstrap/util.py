import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def printRow(row):
	s = ''
	for i in range(len(row)):
		if isNumber(row[i]):
			s += '{:.0f}'.format(float(row[i]))
		else:
			s += str(row[i])
		if i != len(row) - 1:
			s += ' '
	print (s)

def plotHistogram(x, ax=None,block = False,color='green',x_index=101):
	print ('plot')
	# the histogram of the data
	if ax==None:
		n, bins, patches = plt.hist(x, range(101), facecolor=color, alpha=0.75)
		plt.xlabel('Value')
		plt.ylabel('Count')
		plt.grid(True)
		plt.title('Data Histogram')
		return
	else:
		ax.hist(x, range(x_index), facecolor=color, alpha=0.75)

		ax.set_xlabel('Value')
		ax.set_ylabel('Count')
		ax.grid(True)
		ax.set_title('Data Histogram')

	# add a 'best fit' line
	# plt.show(block)

def load(fileName):
	values = []
	with open(fileName) as f:
		for row in f:
			values.append(float(row))
	return values

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
