import numpy as np
import matplotlib.pyplot as plt
n = 100 #number of trials
S = 50
dt = 0.1
k1 = 0.1
k2 = 0.5
k3 = 10.8
k4 = 0.1
X = []
x= 0
for t in range(0,n): #t is an index
    X.append(x)
    x += (k1*S-k2*x)

plt.figure('[X]')
plt.plot(np.arange(0,len(X)),X,color='green',linewidth=3, linestyle='dotted')
plt.title('S=50')
plt.xlabel('t')
plt.ylabel('[X](t)')

R = []
r = 0
for t in range(0,n):
    R.append(r)
    r += k3*S-k4*r*X[t]

plt.figure('[R]')
plt.plot(np.arange(0,len(R)),R,color='red',linewidth=3, linestyle='dotted')
plt.title('S=50')
plt.xlabel('t')
plt.ylabel('[R](t)')
plt.show()
