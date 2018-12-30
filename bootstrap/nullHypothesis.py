import util
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
	pop1 = util.load('p1.csv')
	pop2 = util.load('p2.csv')
	mean1 = np.mean(pop1)
	mean2 = np.mean(pop2)

	totalPop = pop1
	totalPop.extend(pop2)

	# Run a bootstrap experiment
	countDiffGreaterThanObserved = 0
	for i in range(10000):
		sample1 = subsample(totalPop, 100)
		sample2 = subsample(totalPop, 100)
		sampleMean1 = np.mean(sample1)
		sampleMean2 = np.mean(sample2)
		diff = abs(sampleMean2 - sampleMean1)

		if diff > abs(mean1-mean2):
			countDiffGreaterThanObserved += 1
	p = float(countDiffGreaterThanObserved) / 10000
	print ('p-value:', p)

def subsample(original, n):
	sample = []
	for i in range(n):
		v = random.choice(original)
		sample.append(v)
	return sample

def plotHistogram(x, block = True):
	n, bins, patches = plt.hist(x, facecolor='green', alpha=0.75)
	plt.xlabel('Value')
	plt.ylabel('Count')
	plt.grid(True)
	plt.title('Data Histogram')
	plt.show(block)

if __name__ == '__main__':
	main()
