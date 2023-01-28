import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

data = pd.read_csv('RefractiveIndexINFO (1).csv')
print(data)
x = data['um']
y = data['n']

x1 = x[46:59]
y1 = y[46:59]
print(x1)
print(y1)
#plt.plot(x1,y1)
#plt.xlabel(r'$\lambda$($\mu$m)')
#plt.ylabel(r'n')
#plt.show()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x1, y1, color = 'black')
#title = ax.set_title("\n".join(wrap(r"Indice de réfraction n de la silice ($SiO_2$) en fonction de la longueur d'onde $\lambda$", 60)))
fig.tight_layout()
#title.set_y(1.05)
fig.subplots_adjust(top=0.8)
plt.xlabel(r'$\lambda$($\mu$m)')
plt.ylabel(r'n')
ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")
fig.savefig("Graph_Dev1_OptIns.png", bbox_inches='tight',dpi=600)