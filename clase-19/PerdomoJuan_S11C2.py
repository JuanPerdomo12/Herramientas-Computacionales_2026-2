#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

from re import I

import numpy as np
import matplotlib.pylab as plt
from scooby import in_ipykernel


# 1) lea los datos de resorte.dat y almacenelos.

resorte_data = np.genfromtxt("resorte.dat")

t = resorte_data[:, 0]
x = resorte_data[:, 1]

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por  
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  

def modelo_resorte(a, gamma, omega, t):
    return a*np.exp(-gamma*t)*np.cos(omega*t)

# 2b.) Definir una funcion que retorne la funcion de verosimilitud

def verosimilitud(x_obs, x_mod):
    chi_squared = (1.0/2.0)*np.sum((x_obs-x_mod)**2)
    return np.exp(-chi_squared)

# 2c.) Caminata

def metropolis_hastings(a_init, gamma_init, omega_init, pasos):
    datos_a = np.empty(pasos)
    datos_gamma = np.empty(pasos)
    datos_omega = np.empty(pasos)
    L = np.empty(pasos)
    beta = 0.0

    x_mod_init = modelo_resorte(a_init, gamma_init, omega_init, t)

    for i in range(pasos):
        a_newr = np.random.normal(loc=a_init, scale=0.2)
        gamma_newr = np.random.normal(loc=gamma_init, scale=0.02)
        omega_newr = np.random.normal(loc=omega_init, scale=0.4)

        x_mod_newr = modelo_resorte(a_newr, gamma_newr, omega_newr, t)

        L[i] = verosimilitud(x, x_mod_newr)

        alpha = verosimilitud(x, x_mod_newr)/verosimilitud(x, x_mod_init)
        if  alpha >= 1:
            x_mod_init = x_mod_newr
            a_init = a_newr
            gamma_init = gamma_newr
            omega_init = omega_newr
        else:
            beta = np.random.uniform(0, 1)
            if alpha > beta:
                x_mod_init = x_mod_newr
                a_init = a_newr
                gamma_init = gamma_newr
                omega_init = omega_newr
        datos_a[i] = a_init
        datos_gamma[i] = gamma_init
        datos_omega[i] = omega_init

    indice_mejor_modelo = np.argmax(L)

    return datos_a, datos_gamma, datos_omega, indice_mejor_modelo

#condiciones iniciales
aini=7.12
gammaini=0.69
omegaini=18.32

#numero de pasos
iteraciones=100000

a, gamma, omega, i_max = metropolis_hastings(aini, gammaini, omegaini, iteraciones)

# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."

print(f"LOS MEJORES PARAMETROS SON a = {a[i_max]} , gamma = {gamma[i_max]} , Y omega = {omega[i_max]}")

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf

plt.plot(t, x)
plt.plot(t, modelo_resorte(a[i_max], gamma[i_max], omega[i_max], t))
plt.savefig("Resorte.pdf")

# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).



