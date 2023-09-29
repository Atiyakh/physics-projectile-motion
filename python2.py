import matplotlib.pyplot as plt
import numpy as np

R = 240
H = 45

X = list(range(0, R))
y = []

for x in X:y.append(((-H*((x-(R/2))**2))/((R/2)**2))+H)


# plot the function
plt.plot(X,y)
plt.xlim([0, max(X)+0.5])
plt.ylim([0, max(y)+0.5])

# show the plot
plt.show()