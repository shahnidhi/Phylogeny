import sys
import matplotlib.pyplot as plt
import numpy as np
from operator import truediv
from operator import itemgetter

listing = []
bitscore = []
length = []
query = []
sequence = []
percent = []
currentword = 'abc'
flag = 0 

def func():
	global currentword
	global listing
	global length
	global bitscore
	currentword = words[0]
	
	l=[]
	l.append(float(words[2]))
	l.append(words[0])
	l.append(words[1])
	l.append(float(words[3]))
	l.append(float(words[-1]))
	listing.append(l)
	length.append(float(words[3]))
	bitscore.append(float(words[-1]))

if __name__ == "__main__":

	f = open("vsSilva119.blast.out")
	for l in f.readlines():
	  words =  l.strip().split("\t")	 
	  if currentword != words[0]:
	  	func()
	  	#print currentword
	f.close()
	print listing[-1]
	bitdividelength = list(map(truediv, bitscore, length))
	#sorted(listing, key=itemgetter(1))
	listing.sort(key=lambda x: x[0])
	print listing[-1]
	#outarr = np.vstack(listing)
	# save it into a file
	#np.savetxt("test.txt", outarr.T)
	with open ("test.txt","w")as fp:
		for line in listing:
			fp.write(str(line)+"\n")


	#print length
	#print bitscore

