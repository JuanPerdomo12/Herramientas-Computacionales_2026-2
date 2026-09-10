#Escriba un código de eliminación Gaussiana para resolver el sistema Ax=B.

import numpy as np

N=np.random.randint(3, 7)
M=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-5.0

print(f"\n Tamaño: {N}")
print(f"\n Matriz inicial:\n {M}")
print(f"\n Vector constantes inicial:\n {B}")

#compare sus resultados con el paquete de numpy:
#https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

sol_numpy = np.linalg.solve(M, B)
print(f"\n Solucion con numpy:\n {sol_numpy}")

for i in range(N):
    B[i] = B[i]/M[i,i]
    M[i,:] = M[i,:]/M[i,i]
    for j in range(i+1,N):
        B[j] -= B[i]*M[j,i]
        M[j,:] -= M[i,:]*M[j,i]

print(f"\n Matriz triangular superior: \n {M}")
print(f"\n Vector constantes tranformado: \n {B}")

x = np.zeros((N,1))

for k in reversed(range(N)):
    x[k] = B[k] - np.dot(M[k,k+1:], x[k+1:])

print(f"\n Solucion con eliminacion Gaussiana: \n {x}")