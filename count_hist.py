import sys
from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from operator import truediv

listarray=[]
f = open("histogram.txt")
for l in f.readlines():
	word = l.strip()
	listarray.append(float(word))
f.close()

plt.hist(listarray)

plt.xlabel('#hits')
plt.ylabel("#queries")

plt.savefig("hits_count.png")