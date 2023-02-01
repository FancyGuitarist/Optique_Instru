import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt

lama1 = 1*10**(-6)
lama2 = 1.6*10**(-6)
lamb = np.arange(lama1,lama2,0.01*10**(-6))
A1 = 0.696166
lamb1 = 0.068404*10**(-6)
A2 = 0.407942
lamb2 = 0.116241*10**(-6)
A3 = 0.897479
lamb3 = 9.896161*10**(-6)
A = [A1,A2,A3]
Lamb = [lamb1,lamb2,lamb3]
dn2 = A[0]*Lamb[0]**2*(Lamb[0]+3*lamb**3)+A[1]*Lamb[1]**2*(Lamb[1]+3*lamb**3)+A[2]*Lamb[2]**2*(Lamb[2]+3*lamb**3)

#print(dn2)
D = (-lamb/sp.c)*dn2*0.5
print(D)
plt.plot(lamb,D)
plt.show()
#print(2*A[0]*lamb/(lamb**2-Lamb[0]**2)**2)
#print(2*A[0]*lamb/((lamb**2-Lamb[0]**2)**2))