#EJERCICIO 1

#Este ejercicio busca que usted implemente correctamente dos métodos de derivación numérica: forward difference y central difference.
#Pruebe distintos valores de h (que equivale a distintos valores de M).

import numpy as np
import matplotlib.pylab as plt

# Función a derivar
def funcion(x1):
    return np.cos(x1)

#El intervalo de integración es de 0 a 2pi.
#Divida el intervalo de integración en M secciones para calcular sus derivadas.
#pruebe distintos valores de M

# paso 1: use linespace (ver documentación: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
# para hacer el arreglo de su intervalo en x
M=9999
a=0
b=2.0*np.pi

x = np.linspace(a, b, M)

#paso 2: genere el arreglo de valores de su función fx:

fx = funcion(x)

#1) grafique su función para verificar que hizo bien los pasos anteriores

import matplotlib.pyplot as plt

plt.plot(x,fx)

# 2a). Implemente el algoritmo que le permita calcular la derivada de la función para los puntos en el intervalo 0 a 2pi usando forward difference.

h = (b-a)/(M-1)

def deriv_forward(y):
	return (funcion(y+h)-funcion(y))/h

fx_prime_forward = deriv_forward(x)

# 2b). Implemente el algoritmo que le permita calcular la derivada de la función para los puntos en el intervalo 0 a 2pi usando diferencia central.

def deriv_central(y):
	return (funcion(y+h)-funcion(y-h))/(2*h)

fx_prime_central = deriv_central(x)

# 2c). Haga una gráfica de la función y sus derivadas obtenidas usando los dos métodos antes mencionados.

plt.plot(x, fx_prime_forward)
plt.plot(x, fx_prime_central)
plt.show()

# 2d). Haga una grafica con dos subplots (uno por cada metodo) del error |(valor numérico - valor analitico) en el intervalo.

fx_prime_analitic = -np.sin(x)

err_forward = np.abs(fx_prime_forward-fx_prime_analitic)
err_central = np.abs(fx_prime_central-fx_prime_analitic)

plt.plot(x, fx)
plt.subplot(2, 2, 1)
plt.plot(x, err_forward)
plt.subplot(2, 2, 2)
plt.plot(x, err_central)
plt.show()

# 2e). Implemente el algoritmo que le permita calcular la segunda derivada de la función en el intervalo 0 a 2pi. Haga una gráfica de la función y su segunda derivada.

def second_deriv(y):
	return (funcion(y+h)+funcion(y-h)-2*funcion(y))/(h**2)

fx_second_prime = second_deriv(x)

plt.plot(x, fx)
plt.plot(x, fx_second_prime)
plt.show()

# 3) (opcional si terminan el ejercicio 2) Repita el ejercicio anterior usando algunos de los métodos de las librerías de scipy
# https://docs.scipy.org/doc/scipy/tutorial/integrate.html



#EJERCICIO 2

# La idea de este ejercicio es que exploren la convergencia del método de Newton-Raphson para encontrar los ceros del siguiente polinomio:

def poli(x):
    return  (x**5)-(1.7*x**4)-(10.0*x**3)+(20.0*x*x)+ (9.0*x)-18.0

# Para esto:
# 1a.)  Haga una grafica del polinomio en el intervalo [-4:4].

x_pol = np.linspace(-4, 4, M)
pol = poli(x_pol)

plt.plot(x_pol, pol)
plt.show()

# 1b.) Usando su implementación de Newton-Raphson, imprima el valor de una raíz x0_r del polinomio encontrada si usa como x_guess inicial el valor -2.35.
#Imprima el valor de x0_r encontrado y de f(x0_r)

def deriv(f, y):
	return (f(y+h)-f(y-h))/(2*h)

x_0 = -2.35

while np.abs(poli(x_0)) > 1e-10:
	x_0 -= poli(x_0) / deriv(poli, x_0)

print(f"Raíz encontrada: {x_0}. Valor del polinomio en la raíz: {poli(x_0)}")

# 1c.) Repita lo anterior para 1000 valores de x_guess generados aleatoriamente en el intervalo [-4:4].
#Cuente cuantas iteraciones necesita su codigo para encontrar una raiz x_r del polinomio (tal que $f(x_r) sea menor a 10^{-10} para cada x_guess.
#Haga una grafica (use un scatter) del numero de iteraciones en funcion del x_guess inicial.

x_guess = np.random.uniform(-4, 4, 1000)
iterations = []
x_roots = []

for x in x_guess:
	x_r = x
	count = 0
	while np.abs(poli(x_r)) > 1e-10:
		x_r -= poli(x_r) / deriv(poli, x_r)
		count += 1
	iterations.append(count)
	x_roots.append(x_r)

plt.scatter(x_guess, iterations)
plt.show()

# 1c.) Haga una grafica (use un scatter) de la raíz encontrada (en el eje y) en función del x_guess inicial (en el eje x).

plt.scatter(x_guess, x_roots)
plt.show()

# 1d.) Imprima un mensaje en donde explique por que cree que para ciertos valores de x_guess el numero de iteraciones necesarios para encontrar la raiz es mayor.
#Ademas haga un analisis y describa que pasa con los valores de x_r encontrados en esos puntos "problema" comparados con los encontrados para otros valores de x_guess.

print(f"\n El numero de iteraciones aumenta para ciertos valores porque estos corresponden o son muy cercanos a los puntos criticos del polinomio. Como alli la derivada del polinomio se vuelve casi cero el metodo de Newton-Raphson hace que el paso que de sea muy grande y por tanto la convergencia se vuelve mas lenta. Ademas, en estos valores la raiz encontrada puede diferir mucho de la raiz mas cercana por la misma razon del paso grande que da el metodo.")
