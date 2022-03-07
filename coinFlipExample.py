import random
import matplotlib.pyplot as plt
import numpy as np


def flipCoins(nbOfFlips):
    headCount = 0
    tailCount = 0
    for _ in range(nbOfFlips):
        value = random.randint(0, 1)
        if value == 0:
            tailCount += 1
        else:
            headCount += 1
    return [headCount, tailCount]


def experimentFlipCoins(nbOfTest, nbOfFlipPerTest):
    data = []
    for _ in range(nbOfTest):
        results = flipCoins(nbOfFlipPerTest)
        heads = results[0]
        data.append(heads)

    return data


nbOfTest = 10000
nbOfFlips = 1000
trialData = experimentFlipCoins(nbOfTest, nbOfFlips)
freq = [trialData.count(k) for k in range(nbOfFlips)]

x = np.linspace(0, 1, nbOfFlips)
plt.bar(x, freq, width=0.01)
plt.show()
