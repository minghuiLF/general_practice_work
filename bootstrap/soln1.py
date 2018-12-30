import population
import numpy as np
import random
import util
import math
import matplotlib.pyplot as plt

NPOP = 10000
NSAMPLE = 15

def main():
	print ('\nTesting Sample Variance\n')

	# Get a random population
	pop = population.makeModalPopulation(NPOP)
	util.plotHistogram(pop)

	unbiasedVars = []
	biasedVars = []
	for i in range(10000):
		sample = random.sample(pop, NSAMPLE)

		# Calculate the unbiased estimate of variance
		unbiased = calcSampleVariance(sample)
		unbiasedVars.append(unbiased)

		# Calculate the biased estimate of variance
		biased = calcVariance(sample)
		biasedVars.append(biased)

		# print (unbiased)


	# What is the expectation of sampleVar?
	print ('\n')
	printRow(['E[biased var]:   ', np.mean(biasedVars)])
	printRow(['E[unbiased var]: ',np.mean(unbiasedVars)])
	printRow(['true var:        ',calcVariance(pop)])



# This is the definition of the variance of an
# entire population.
def calcSampleVariance(data):
	sampleMean = np.mean(data)
	n = len(data)
	total = 0
	for i in range(n):
		d = data[i]
		total += math.pow(d - sampleMean, 2)
	return float(total)/ (n-1)

# This is the definition of the variance of an
# entire population.
def calcVariance(data):
	sampleMean = np.mean(data)
	n = len(data)
	total = 0
	for i in range(n):
		d = data[i]
		total += math.pow(d - sampleMean, 2)
	return float(total)/ (n)

def printRow(row):
	util.printRow(row)

if __name__ == '__main__':
	main()
	plt.show()
