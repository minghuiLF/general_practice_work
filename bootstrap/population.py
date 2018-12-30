import random

def makeRandomPopulation(n):
	pmf = getRandomPmf()
	return samplePmf(pmf, n)

def makeModalPopulation(n):
	pmf = getModalPmf()
	return samplePmf(pmf, n)

def samplePmf(pmf, n):
	cdf = makeCdf(pmf)
	pop = []
	for i in range(n):
		v = drawSample(cdf)
		pop.append(v)
	return pop

def getModalPmf():
	unnormalized = []
	currValue = 0
	derivative = 0
	secondDerivative = random.random()
	for i in range(100):
		if i % 25 == 0:
			secondDerivative = random.random()
			secondDerivative *= -1
		derivative += secondDerivative
		currValue += derivative
		if currValue < 0:
			secondDerivative = random.random() - 0.5
			derivative = 0
			currValue = 0
		unnormalized.append(currValue)
	total = sum(unnormalized)
	dist = []
	for i in range(len(unnormalized)):
		dist.append(unnormalized[i] / total)
	return dist

def getRandomPmf():
	unnormalized = []
	for i in range(100):
		unnormalized.append(random.random())
	total = sum(unnormalized)
	dist = []
	for i in range(len(unnormalized)):
		dist.append(unnormalized[i] / total)
	return dist

def makeCdf(pmf):
	cdf = []
	cumulative = 0
	for i in range(len(pmf)):
		cumulative += pmf[i]
		cdf.append(cumulative)
	return cdf

def drawSample(cdf):
	y = random.random()
	v = binarySearch(cdf, y)
	return v

def binarySearch(cdf, goalY):
	lowerIndex = 0
	upperIndex = len(cdf)
	# print(1)
	while True:
		midIndex = lowerIndex + (upperIndex - lowerIndex)/2
		# print (lowerIndex, midIndex, upperIndex)

		y = cdf[int(midIndex)]
		if y < goalY:
			lowerIndex = int(midIndex)
		else:
			upperIndex = int(midIndex)
		spread = upperIndex - lowerIndex
		if spread == 1:
			if goalY > cdf[lowerIndex]:
				return upperIndex
			else:
				return lowerIndex
