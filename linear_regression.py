#Linear regression
import numpy as np
import csv2array
import matplotlib.pyplot as plt

infile = input("Enter a csv filename: ")

ar = csv2array.csvar(infile)

# Training
X = ar[:,0]
Y = ar[:,1]
m = X.shape[0]	#number of training examples
epoch = 150000  #number of iterations
t0 = 0.9999
t1 = 0.9999
alpha = 0.00009
i = 0
while (i<epoch):
	h = float(t0) + (float(t1)*X)	#hypothesis
	dif = h - Y     #cost function
	#gradient descent
	t0 = t0 - alpha*(1/(m) * (sum(dif)))
	t1 = t1 - alpha*(1/(m) * (sum(dif*X)))
	print("epoch=",i,"t0=",t0,"t1=",t1)
	i += 1

#################

#Testing data

testf = input("Enter test filename: ")
ar2 = csv2array.csvar(testf)
x = ar2[:,0]
y = ar2[:,1]
h1 = float(t0) + (float(t1)*x)
plt.scatter(ar2[:,0],ar2[:,1],s = 5)
plt.title("Linear Regression Testing")
plt.xlabel("x")
plt.xlabel("y")
plt.plot(x,h1,color = 'black')
plt.show()
