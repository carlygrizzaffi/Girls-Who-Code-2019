import numpy as np
import matplotlib.pyplot as plt
import random
from numpy.random import RandomState

def randomwalk(k):
    position = 0
    mysteps = []
    for n in range(0,k):
        positoin += random.choice(np.array([1,-1]))
        mysteps.append(position)
    return(mysteps)

k = 500
xrange = []

for x in range(0,k,1):
    xrange.append(x)

plt.scatter(xrange,[randomwalk(k)], s = 1, color = 'majenta')
plt.scatter(xrange,[randomwalk(k)], s = 1, color = 'blue')
plt.scatter(xrange,[randomwalk(k)], s = 1, color = 'brown')

plt.xlim([0,500])
plt.title("Random Walk Generator")
plt.xlabel("# Steps")
plt.ylabel("Position")
plt.show()
#Clear out memory
plt.close()

#Make a histogram
gaussian_numbers = np.random.randn(1000)
plt.hist(gaussian_numbers, bins = 20, color = "pink")
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequeny")
plt.show()

plt.close()
