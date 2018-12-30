import scipy.stats as stats
import random

def bern(p):
	event = random.random() < p
	if event: return 1
	else: return 0

def norm(mu, std):
	return stats.norm.rvs(mu, std)

def normPdf(x, mu, std):
	return stats.norm.pdf(x, mu, std)