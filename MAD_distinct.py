import sys

from math import fabs
import matplotlib.pyplot as plt
import numpy as np
from operator import truediv
from  more_itertools import unique_everseen

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
bitsorted = list(unique_everseen(bitsorted))
#print sorted(bitsorted)
#print len(bitsorted)
med = sorted(bitsorted)[len(bitsorted)//2]

print med
test_distinct=[]
for test in bitsorted:
  mad = fabs(float(test) - float(med))
  test_distinct.append(mad)
#print test_distinct
mad_test = sorted(test_distinct)[len(test_distinct)//2]
print mad_test

#i=0
#for b in bitscore:
#    mad = fabs(float(b) - float(med))
#    listing[i].append(mad)
#    i = i + 1
#A = np.array(listing)
#absbit = list(A[:,-1])
#map(float,absbit)
#absbit = [float(i) for i in absbit]
#absbitsort  = absbit
#absbitsort= list(unique_everseen(absbitsort))
#print absbitsort
#madfinal = sorted(absbitsort)[len(absbitsort)//2]
#print sorted(absbit)
#print madfinal

plt.figure(1)
plt.ylabel("Bitscore")
plt.xlabel(number)
i=0
outlier = 3.0
#outlier = 1.4826
with open ("outlier95.txt","a")as fp:
	for line in listing:
		if (float(line[-1]) > float(med) + outlier*float(mad_test) ) or (float(line[-1]) < float(med) - outlier*float(mad_test)):
	#	if (float(line[-2]) > float(med) + 2.5*float(madfinal) ) or (float(line[-2]) < float(med) - 2.5*float(madfinal)):
			plt.plot(i,line[-1],'ro')
			fp.write(str(line)+"\n")
		else:
			plt.plot(i,line[-1],'go')
		i = i + 1
plt.savefig('tmp/mad_distinct/bitscore_outlier-'+str(outlier)+'_'+number+'.png')
plt.show()
