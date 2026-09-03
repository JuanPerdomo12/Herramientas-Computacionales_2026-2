#Este ejercicio preparatorio busca que usted implemente correctamente tres métodos de integración numérica. Pruebe distintos valores de h. Si termina el ejercicio antes de que acabe la clase, repita el proceso para el método de Monte Carlo y el método del valor medio.

import numpy as np
import matplotlib.pylab as plt

# Función a integrar
def funcion(x1):
    return np.cos(x1)

#El intervalo de integración es de 0 a 3pi/2.
#Divida el intervalo de integración en M secciones para calcular sus integrales.
#pruebe distintos valores de M

# paso 1: use linespace (ver documentación: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
# para hacer el arreglo de su intervalo en x
M=9999
a=0
b=3*np.pi/2

x = np.linspace(a, b, M)

#paso 2: genere el arreglo de valores de su función fx:

fx = funcion(x)

#1) grafique su función para verificar que hizo bien los pasos anteriores

import matplotlib.pyplot as plt

plt.plot(x,fx)
plt.show()

# 2a). Usando el método de suma de rectángulos, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.

h = (b-a)/(M-1)

def Riemann(funcion):
	return h * np.sum(funcion)

Int_riemann = Riemann(fx)

Int_analitica = -1

print(f"\n Integral de riemann numerica es: {Int_riemann}. La integral analitica es: {Int_analitica}")

# 2b). Usando el método de trapezoide, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.

def trapecio(funcion):
      return h/2 * funcion[0] + h * np.sum(funcion[1:-1]) + h/2 * funcion[-1]

Int_trapecio = trapecio(fx)

print(f"\n Integral de trapecio numerica es: {Int_trapecio}. La integral analitica es: {Int_analitica}")

# 2c). Usando el método de Simpson, calcule la integral de la función.
#Compare su valor obtenido numéricamente con el valor analitico e imprima ambos valores.

def simpson(funcion):
    return h/3 * funcion[0] + h/3 * funcion[-1] + 2*h/3 * np.sum(funcion[2:-2:2]) + 4*h/3 * np.sum(funcion[1:-1:2])

Int_simpson = simpson(fx)

print(f"\n Integral de simpsoon numerica es: {Int_simpson}. La integral analitica es: {Int_analitica}")

# 3a)Repita el ejercicio anterior usando algunos de los métodos de las librerías de scipy
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html

from scipy.integrate import trapezoid, simpson

Int_scipy_trapecio = trapezoid(fx, x)
Int_scipy_simpson = simpson(fx, x = x)

print(f"\n Integral de trapecio con scipy es: {Int_scipy_trapecio}. La integral analitica es: {Int_analitica}")
print(f"\n Integral de simpson con scipy es: {Int_scipy_simpson}. La integral analitica es: {Int_analitica}")

# 3b)OPCIONAL: Repita el ejercicio anterior usando el método de Monte Carlo y/o el del valor medio (ver diapositivas)

N = 10000

x_random = np.random.uniform(a, b, N)

evaluar = funcion(x_random)

Int_Valor_medio = (b-a) * np.mean(evaluar)

print(f"\n Integral de valor medio (con N = {N}) es: {Int_Valor_medio}. La integral analitica es: {Int_analitica}")

fx = funcion(x_random)

y_min = np.min(fx)
y_max = np.max(fx)

y_random = np.random.uniform(y_min, y_max, N)

puntos_positivos = (y_random <= fx) & (y_random >= 0)
puntos_negativos = (y_random >= fx) & (y_random <= 0)

proporcion = ((np.sum(puntos_positivos) - np.sum(puntos_negativos)))/N

area_total = (b-a) * (y_max - y_min)

Int_MonteCarlo = area_total * proporcion

print(f"\n Integral de Monte Carlo (con N = {N}) es: {Int_MonteCarlo}. La integral analitica es: {Int_analitica}")