#Convert a csv file to array
import csv
import numpy as np

def csvar(infile):
	i = infile
	f = open(i)
	read = csv.reader(f)
	print(f)
	a = []
	for r in read:
		a.append(r)
	a.pop(0)
	ar = np.asarray(a,dtype = float)
	return ar