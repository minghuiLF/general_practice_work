from util import *
import copy

N_BURN = 0
N_SAMPLES = 100000

UND_I = 0
TIR_I = 1

# samples are vectors of length four:
# [flu, und, fev, tir]
def main():
	undObs = None
	tirObs = None
	obs = [undObs, tirObs]
	print 'Observation = ', obs

	samples = mcmcSamples(obs)
	prob = probUnd(samples)
	print 'Pr(Und) = ', prob

def probUnd(samples):
	# from remaining, simply count...
	count = 0
	for sample in samples:
		print sample
		[und, tir] = sample
		if und == 1:
			count += 1
	return float(count) / len(samples)

def mcmcSamples(obs):
	intialSample = getInitialSample(obs)
	prevSample = intialSample
	samples = []
	for i in range(N_SAMPLES):
		sample = getJointSample(prevSample, obs)
		if i > N_BURN:
			samples.append(sample)
		prevSample = sample
	return samples

def getInitialSample(obs):
	sample = []
	for i in range(len(obs)):
		if obs[i] != None:
			sample.append(obs[i])
		else:
			sample.append(0)
	return sample

def getJointSample(prevSample, obs):
	sample = copy.deepcopy(prevSample)
	for i in range(len(sample)):
		if obs[i] == None:
			sample[i] = sampleValue(i, sample)
	return sample

def sampleValue(i, sample):
	if i == UND_I: return sampleUnd(sample)
	if i == TIR_I: return sampleTir(sample)
	raise Exception('unknown index ' + str(i))

def sampleTir(sample):
	und = sample[UND_I]
	prTired = getPrTired1(und)
	return bern(prTired)

def sampleUnd(sample):
	u1 = getUndPr1(sample)
	u0 = getUndPr0(sample)
	p1 = u1 / (u1 + u0)
	# print sample
	# print u0, u1, p1
	# raise Exception('test')
	return bern(p1)

def getUndPr0(sample):
	tir = sample[TIR_I]
	pUnd0 = 0.2
	pTir = getPrTired(tir, 0)
	return pUnd0 * pTir

def getUndPr1(sample):
	tir = sample[TIR_I]
	pUnd1 = 0.8
	pTir = getPrTired(tir, 1)
	return pUnd1 * pTir

def getPrTired(tir, und):
	p1 = getPrTired1(und)
	if tir == 1: 
		return p1
	else:
		return 1- p1

def getPrTired1(und):
	if und == 1: return 0.5
	else:	return 0.3
if __name__ == '__main__':
	main()