#ejercicio 1

print(f"ejercicio 1")

#a) Inicializar dos variables globales (con valores escogidos por ustedes), una entera y otra flotante.\\

x = 12
y = 95.44

#b) Imprimir los valores de las variables en un mensaje: #
#"la primera tiene un valor de XX y la segunda variable tiene un valor de YY"

print(f"\n la primera tiene un valor de {x} y la segunda variable tiene un valor de {y}")

#c) Calcular el valor de la segunda variable dividida por la primera e imprimir : "El resultado es ZZ"

z = y/x

print(f"\n El resultado es {z}")

#d) Crear una lista con los elementos: 101, 45, 26, rio, gato, 17, 45 y 28 e imprimirla.

lista_1=[101, 45, 26, "rio", "gato", 17, 45, 28]

print(f"\n {lista_1}\n")

#e) Agregarle a esa lista los elementos: 257, 285, 583

lista_2 = [257, 285, 583]
lista_3 = lista_1 + lista_2

#f) Hacer un ciclo para recorrer dicha lista e imprimir sus elementos.

for i in lista_3:
    print(f"i: {i}")


#g) imprimir el cuarto elemento de la lista (que en este caso sería "rio").

print(f"\n {lista_3[3]}")

#h) Calcular la longitud de la lista e imprimir: "la longitud de la lista es XX" puede usar le función len()

longitud = len(lista_3)

print(f"\n la longitud de la lista es {longitud}")


#ejercicio 2
# Complete el siguiente código para que:
# recorra el arreglo `x`
# imprima los números impares
# y pare de imprimir al encontrar un número mayor a 800

import numpy as np

#genero un arreglo de número aleatorios:

xx=np.int_(np.random.random(100)*1000)
print(f"\n arreglo x: {xx}")

for i in xx: 
    if((xx[i]%2) != 0):
        print(xx[i])


#ejercicio 3
print("ejercicio 3")

#Haga una función llamada multiplicación
#que reciba como argumentos dos variables a y b y retorne a*b.
#Imprima lo que retorna la función para a=10 y b=18


#ejercicio 4
print("ejercicio 4")
# Complete el siguiente código para que:
# recorra la lista x del ejercicio 2 y encuentre el mínimo de los elementos de la lista.
#Compare su resultado con el obtenido por np.min e imprima un mensajito con ambos valores.


#ejercicio 5
print("ejercicio 5")
#  sin usar ciclos, sume los 10 primeros elementos del arreglo x a los 10 últimos elementos del arreglo x. Imprima el arreglo resultante.
import numpy as np

#genero un arreglo de número aleatorios:
x=np.int_(np.random.random(100)*900)
print("arreglo x: ", x)