import sys
import matplotlib.pyplot as plt
import numpy as np
from operator import truediv
from operator import itemgetter

if __name__ == "__main__":

	listing = [[2,3,4],[1,2,3],[0,1,3]]
	print listing
	#sorted(listing, key=itemgetter(0))
	listing.sort(key=lambda x: x[0])
	print listing
	

