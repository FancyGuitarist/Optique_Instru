import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('RefractiveIndexINFO (1).csv')
print(data)
x = data['um']
y = data['n']

x1 = x[46:59]
y1 = y[46:59]
print(x1)
print(y1)
plt.plot(x1,y1)
plt.xlabel(r'$\lambda$($\mu$m)')
plt.ylabel(r'n')
plt.show()