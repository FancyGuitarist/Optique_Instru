import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt

lambdas = [1,1.1,1.2,1.3,1.4,1.5,1.6]
A1 = 0.696166
lamb1 = 0.068404
A2 = 0.407942
lamb2 = 0.116241
A3 = 0.897479
lamb3 = 9.896161
A = [A1,A2,A3]
Lamb = [lamb1,lamb2,lamb3]
N = []
n = 0
for i in range(len(lambdas)):
    n = (1+((A[0]*(lambdas[i]**2))/((lambdas[i]**2)-(Lamb[0]**2)))+((A[1]*(lambdas[i]**2))/((lambdas[i]**2)-(Lamb[1]**2)))+((A[2]*(lambdas[i]**2))/((lambdas[i]**2)-(Lamb[2]**2))))**(1/2)
    N.append(n)
print(N)

x1 = lambdas
y1 = N

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
