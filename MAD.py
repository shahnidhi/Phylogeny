import sys
from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from operator import truediv
flag = 0
number = sys.argv[1]
listing=[]
f = open("vsSilva119.blast.out")
for l in f.readlines():
  words =  l.strip().split("\t")
  if words[0] == number:
  	flag = 1
  	listing.append(words)
  elif flag:
  	break
f.close()
A = np.array(listing)
bitscore = list(A[:,-1])
#map(float,bitscore)
bitscore = [float(i) for i in bitscore]
bitsorted = bitscore
med = sorted(bitsorted)[len(bitscore)//2]
#print sorted(bitscore)
print med
i=0
for b in bitscore:
    mad = fabs(float(b) - float(med))
    listing[i].append(mad)
    i = i + 1
A = np.array(listing)
absbit = list(A[:,-1])
#map(float,absbit)
absbit = [float(i) for i in absbit]
absbitsort  = absbit
madfinal = sorted(absbitsort)[len(absbitsort)//2]
#print sorted(absbit)
print madfinal

plt.figure(1)
plt.ylabel("Bitscore")
plt.xlabel(number)
i=0
outlier = 3.0
#outlier = 1.4826
with open ("outlier95.txt","a")as fp:
	for line in listing:
		if (float(line[-2]) > float(med) + outlier*float(madfinal) ) or (float(line[-2]) < float(med) - outlier*float(madfinal)):
	#	if (float(line[-2]) > float(med) + 2.5*float(madfinal) ) or (float(line[-2]) < float(med) - 2.5*float(madfinal)):
			plt.plot(i,line[-2],'ro')
			fp.write(str(line)+"\n")
		else:
			plt.plot(i,line[-2],'bo')
		i = i + 1
plt.savefig('tmp/95/bitscore_outlier-'+str(outlier)+'_'+number+'.png')
plt.show()
