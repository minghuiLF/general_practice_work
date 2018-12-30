from util import *
import copy

N_BURN = 0
N_SAMPLES = 100000
FLU_I = 0
UND_I = 1
FEV_I = 2
TIR_I = 3

# samples are vectors of length four:
# [flu, und, fev, tir]
def main():
	fevObs = None
	fluObs = None
	undObs = None
	tirObs = 1
	obs = [fluObs, undObs, fevObs, tirObs]
	print ('Observation = ', obs)

	samples = mcmcSamples(obs)
	prob = probFlu(samples)
	print ('Pr(Flu) = ', prob)

def probFlu(samples):
	# from remaining, simply count...
	fluCount = 0
	for sample in samples:
		print (sample)
		[flu, und, fev, tir] = sample
		if flu == 1:
			fluCount += 1
	return float(fluCount) / len(samples)

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
	if i == FLU_I: return sampleFlu(sample)
	if i == UND_I: return sampleUnd(sample)
	if i == FEV_I: return sampleFev(sample)
	if i == TIR_I: return sampleTir(sample)

def sampleFev(sample):
	flu = sample[FLU_I]
	prFever = getPrFever1(flu)
	return bern(prFever)

def sampleTir(sample):
	und = sample[UND_I]
	flu = sample[FLU_I]
	prTired = getPrTired1(und, flu)
	return bern(prTired)

def sampleUnd(sample):
	u1 = getUndPr1(sample)
	u0 = getUndPr0(sample)
	p1 = u1 / (u1 + u0)
	return bern(p1)

def sampleFlu(sample):
	f1 = getFluPr1(sample)
	f0 = getFluPr0(sample)
	p1 = f1 / (f1 + f0)
	return bern(p1)

def getFluPr0(sample):
	[_, und, fev, tir] = sample
	pFlu0 = 0.9
	pFev = getPrFeverX(fev, 0)
	pTir = getPrTiredX(tir, und, 0)
	return pFlu0 * pFev * pTir

def getFluPr1(sample):
	[_, und, fev, tir] = sample
	pFlu1 = 0.1
	pFev = getPrFeverX(fev, 1)
	pTir = getPrTiredX(tir, und, 1)
	return pFlu1 * pFev * pTir

def getUndPr0(sample):
	[flu, _, fev, tir] = sample
	pUnd0 = 0.2
	pTir = getPrTiredX(tir, 0, flu)
	return pUnd0 * pTir

def getUndPr1(sample):
	[flu, _, fev, tir] = sample
	pUnd1 = 0.8
	pTir = getPrTiredX(tir, 1, flu)
	return pUnd1 * pTir

def getPrFeverX(x, flu):
	p1 = getPrFever1(flu)
	return (p1 if x == 1 else 1 - p1)

def getPrTiredX(x, und, flu):
	p1 = getPrTired1(und, flu)
	return (p1 if x == 1 else 1 - p1)

def getPrFever1(flu):
	if flu == 1:
		return 0.9
	else:
		return 0.05

def getPrTired1(und, flu):
	if und == 1 and flu == 1:
		return 1.0
	elif und == 1 and flu == 0:
		return 0.8
	elif und == 0 and flu == 1:
		return 0.9
	else:
		return 0.1

if __name__ == '__main__':
	main()
