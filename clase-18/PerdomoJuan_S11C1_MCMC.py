# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt

# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion.

def mifun(x):
	x_0 = 3.0
	a = 0.01
	return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar 
# para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de 
# los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). 
# Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y 
# pasos son los parametros que recibe la funcion.

def metropolis_hastings(sigma, pasos, f):
    x_r = np.random.uniform(-4, 4)
    datos = np.empty(pasos)
    beta = 0.0

    for i in range(pasos):
        x_nr = np.random.normal(loc=x_r, scale=sigma)
        alpha = f(x_nr)/f(x_r)
        if  alpha >= 1:
            x_r = x_nr
        else:
            beta = np.random.uniform(0, 1)
        if alpha > beta:
            x_r = x_nr
        datos[i] = x_r

    x = np.linspace(-4, 4, 1000)
    y = f(x)
    y = y / np.trapezoid(y, x)
    plt.hist(datos, bins=100, density=True)
    plt.plot(x, y)
    plt.savefig("histograma_" + str(sigma) + "_" + str(pasos) + ".pdf")
    plt.close()
    return datos

# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000
# sigma = 0.2, pasos =100000
# sigma = 0.01, pasos =100000
# sigma = 0.1, pasos =1000
# sigma = 0.1, pasos =100000
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000

ej1 = metropolis_hastings(5, 100000, mifun)
ej2 = metropolis_hastings(0.2, 100000, mifun)
ej3 = metropolis_hastings(0.01, 100000, mifun)
ej4 = metropolis_hastings(0.1, 1000, mifun)
ej5 = metropolis_hastings(0.1, 100000, mifun)
ej6 = metropolis_hastings(0.1, 500000, mifun)

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.