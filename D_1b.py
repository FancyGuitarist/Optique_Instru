import numpy as np
import scipy.constants as sp
import matplotlib.pyplot as plt

lama1 = 1
lama2 = 1.6
lamb = np.arange(lama1,lama2,0.01)
A1 = 0.696166
lamb1 = 0.068404
A2 = 0.407942
lamb2 = 0.116241
A3 = 0.897479
lamb3 = 9.896161
A = [A1,A2,A3]
Lamb = [lamb1,lamb2,lamb3]
dn2 = (A1*(lamb1**2)*((lamb1**2)+3*(lamb**3)))/(((lamb**2)-(lamb1**2))**3) + (A2*(lamb2**2)*((lamb2**2)+3*(lamb**3)))/(((lamb**2)-(lamb2**2))**3) + (A3*(lamb3**2)*((lamb3**2)+3*(lamb**3)))/(((lamb**2)-(lamb3**2))**3)

#print(dn2)
D = (-lamb/(sp.c*10**(6)))*dn2
print(sp.c)
print(dn2)
print(D)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(lamb, D, color = 'black')
fig.tight_layout()
fig.subplots_adjust(top=0.8)
plt.xlabel('$\lambda$($\mu$m)')
plt.ylabel('D')
ax.tick_params(axis="y",direction="in")
ax.tick_params(axis="x",direction="in")
fig.savefig("1B_Optique", bbox_inches='tight',dpi=600)
#print(2*A1*lamb/(lamb**2-Lamb[0]**2)**2)
#print(2*A1*lamb/((lamb**2-Lamb[0]**2)**2))