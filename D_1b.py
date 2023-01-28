import numpy as np
import scipy.constants as sp

lamb = 1.6*(10**(-6))
A1 = 0.696166
lamb1 = 0.068404*(10**(-6))
A2 = 0.407942
lamb2 = 0.116241*(10**(-6))
A3 = 0.897479
lamb3 = 9.896161*(10**(-6))
A = [A1,A2,A3]
Lamb = [lamb1,lamb2,lamb3]
D = 0
for i in range(2):
    D += (1+((2*A[i])/(lamb**2-Lamb[i]**2))-((A[i]*(4*lamb-1))/4*lamb))**(-3/2)
D = D*(lamb/(4*sp.c))
print(D)