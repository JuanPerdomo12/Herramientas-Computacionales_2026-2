#ejercicio 1

print(f"\n --------------------------------------------------------------------------")
print(f"ejercicio 1")

#a) Inicializar dos variables globales (con valores escogidos por ustedes), una entera y otra flotante.\\

x = 12
y = 95.44

#b) Imprimir los valores de las variables en un mensaje: #
#"la primera tiene un valor de XX y la segunda variable tiene un valor de YY"

print(f"\n La primera tiene un valor de {x} y la segunda variable tiene un valor de {y}")

#c) Calcular el valor de la segunda variable dividida por la primera e imprimir : "El resultado es ZZ"

z = y/x

print(f"\n El resultado de dividir {y} entre {x} es {z}")

#d) Crear una lista con los elementos: 101, 45, 26, rio, gato, 17, 45 y 28 e imprimirla.

lista_1=[101, 45, 26, "rio", "gato", 17, 45, 28]

print(f"\n {lista_1}\n")

#e) Agregarle a esa lista los elementos: 257, 285, 583

lista_2 = [257, 285, 583]
lista_3 = lista_1 + lista_2

#f) Hacer un ciclo para recorrer dicha lista e imprimir sus elementos.

for i in lista_3:
    print(f"{i}")


#g) imprimir el cuarto elemento de la lista (que en este caso sería "rio").

print(f"\n El cuarto elemento es: {lista_3[3]}")

#h) Calcular la longitud de la lista e imprimir: "la longitud de la lista es XX" puede usar le función len()

longitud = len(lista_3)

print(f"\n La longitud de la lista es {longitud}")


#ejercicio 2
# Complete el siguiente código para que:
# recorra el arreglo `xx`
# imprima los números impares
# y pare de imprimir al encontrar un número mayor a 800

import numpy as np

#genero un arreglo de número aleatorios:

print(f"\n --------------------------------------------------------------------------")
print(f"\n ejercicio 2")

xx=np.int_(np.random.random(100)*1000)
print(f"\n arreglo x: {xx}\n")

for i in range (len(xx)): 
    if((xx[i]%2) != 0):
        print(xx[i])

print(f"\n")

for i in range (len(xx)): 
    if((xx[i]%2) != 0):
        if(xx[i] > 800):
            break
        print(xx[i])


#ejercicio 3

print(f"\n --------------------------------------------------------------------------")
print(f"\n ejercicio 3")

#Haga una función llamada multiplicación
#que reciba como argumentos dos variables a y b y retorne a*b.
#Imprima lo que retorna la función para a=10 y b=18

def multiplicacion(a, b):
    return a*b

a = 10
b = 18

print(f"\n La multiplicacion de {a} y {b} es: {multiplicacion(a,b)}")

#ejercicio 4

print(f"\n --------------------------------------------------------------------------")
print(f"\n ejercicio 4")

# Complete el siguiente código para que:
# recorra la lista xx del ejercicio 2 y encuentre el mínimo de los elementos de la lista.
#Compare su resultado con el obtenido por np.min e imprima un mensajito con ambos valores.

minimo = xx[0]
for i in range (len(xx)):
    if xx[i] < minimo:
        minimo = xx[i]

print(f"\n El mínimo de la lista con el codigo es: {minimo}. Usando np.min es: {np.min(xx)}")

#ejercicio 5

print(f"\n --------------------------------------------------------------------------")
print(f"\n ejercicio 5")

#sin usar ciclos, sume los 10 primeros elementos del arreglo xy a los 10 últimos elementos del arreglo xy. Imprima el arreglo resultante.
#genero un arreglo de número aleatorios:

xy=np.int_(np.random.random(100)*900)
print(f"\n arreglo xy: ", xy)

resultante = xy[:10] + xy[-10:]
print(f"\n arreglo resultante: ", resultante)