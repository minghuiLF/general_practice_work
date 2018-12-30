from util import *

N_SAMPLES = 100000

# Program: Joint Sample Continuous
# ---------------------
# we can answer any probability question
# with multivariate samples from the joint,
# where conditioned variables match. However
# this program demonstrates that this strategy
# break downs for rare events (such as a continuous
# random variable taking on a specific value)
def main():
	# make an observation to condition on
	fevObs = 99.2
	fluObs = None
	undObs = None
	tirObs = None
	obs = [fluObs, undObs, fevObs, tirObs]

	# sample from the joint
	samples = sampleATon()

	# calculate a probability from joint samples
	prob = probFluGivenObs(samples, obs)
	print ('Observation = ', obs)
	print ('Pr(Flu) = ', prob)

# Method: Probability of Flu Given Observation
# --------------------------
# Calculate the probability of flu given many
# samples from the joint distribution and a set
# of ovservations to condition on.
def probFluGivenObs(samples, obs):
	# reject all samples which don't align
	# with condition
	keepSamples = []
	for sample in samples:
		if checkObsMatch(sample, obs):
			keepSamples.append(sample)

	# from remaining, simply count...
	fluCount = 0
	for sample in keepSamples:
		[flu, und, fev, tir] = sample
		if flu == 1:
			fluCount += 1

	return float(fluCount) / len(keepSamples)

# Method: Check Observation Match
# -------------------------------
# returns true if and only if the random vars in
# the sample matches with the observed random vars
# for example:
# sample = [1,    0,    98.4, 1]
# obs =    [None, None, 99.2, None]
# checkObsMatch(sample, obs) will return False
# since the only observed var (the thrid one) does not match
def checkObsMatch(sample, obs):
	[fluObs, undObs, fevObs, tirObs] = obs
	[fluSam, undSam, fevSam, tirSam] = sample

	# checks if each value matches
	for i in range(len(obs)):
		varObs = obs[i]
		varSam = sample[i]
		# only check if the observation is not None
		if varObs != None and varObs != varSam:
			# return False if there is any mismatch
			return False
	# return true if all tests pass
	return True

# Method: Sample A Ton
# --------------------
# chose N_SAMPLES with likelhood proportional
# to the joint distribution
def sampleATon():
	samples = []
	for i in range(N_SAMPLES):
		sample = makeSample()
		print (sample)
		samples.append(sample)
	return samples

# Method: Make Sample
# -------------------
# chose a single sample from the joint distribution
# based on the medical "Probabilistic Graphical Model"
def makeSample():
	# prior on causal factors
	flu = bern(0.1)
	und = bern(0.8)

	# choose fever
	if flu == 1:
		fev = norm(100.0, 1.81)
	else:
		fev = norm(98.25, 0.73)

	# choose tired
	if und == 1 and flu == 1:
		tir = bern(1.0)
	elif und == 1 and flu == 0:
		tir = bern(0.8)
	elif und == 0 and flu == 1:
		tir = bern(0.9)
	else:
		tir = bern(0.1)

	# a sample from the joint has an
	# assignment to *all* random variables
	return [flu, und, fev, tir]


if __name__ == '__main__':
	main()
