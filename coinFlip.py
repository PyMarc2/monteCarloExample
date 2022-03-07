import random
import matplotlib.pyplot as plt
import numpy as np


def coinFlips(nbOfFlips):
    tailsCount = 0
    headsCount = 0
    for _ in range(nbOfFlips):
        if random.randint(0, 1) == 0:
            tailsCount += 1
        else:
            headsCount += 1
    return headsCount, tailsCount

def coinExperimentCountHeads(nbOfTrials, nbOfFlipsPerTrial):
    trialData = []
    for _ in range(nbOfTrials):
        headsCount, tailsCount = coinFlips(nbOfFlipsPerTrial)
        trialData.append(headsCount)
    return trialData


nbOfFlips = 100
nbOfTrials = 1000
trialData = coinExperimentCountHeads(nbOfTrials, nbOfFlips)
print(trialData)
freq = [trialData.count(k) for k in range(nbOfFlips)]
print(freq)
x = np.linspace(0, 1, nbOfFlips)
plt.bar(x, freq, align='center', width=0.01)
plt.xlabel(r"Sum of N flip / nb of flip")
plt.ylabel("Counts")
plt.show()
