import sys
import matplotlib.pyplot as plt
from operator import truediv

number = sys.argv[1]
bitscore = []
length = []
flag = 0 
f = open("vsSilva119.blast.out")
for l in f.readlines():
  words =  l.strip().split("\t")
  if words[0] == number:
  	flag = 1
  	length.append(float(words[3]))
  	bitscore.append(float(words[-1]))
  elif flag:
  	break
f.close()
bitdividelength = list(map(truediv, bitscore, length))
#print length
print bitscore
plt.figure(1)
plt.ylabel("Bitscore")
plt.xlabel(number)
plt.plot(bitscore,'ro',label='top 100 hits bitscore')
plt.savefig('bitscore'+number+'.pdf')
plt.figure(2)
plt.ylabel("Bitscore/ Alignment-length")
plt.xlabel(number)
plt.plot(bitdividelength,'ro',label='top 100 hits bitscore/Alignment-length')
plt.savefig('bit_alignlen'+number+'.pdf')

