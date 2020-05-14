"""
lista=[2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)

Como podemos ver la instrucción for requiere una variable (en este ejemplo llamada elemento), 
luego la palabra clave in y por último el nombre de la lista. El bloque del for se ejecuta 
tantas veces como elementos tenga la lista, y en cada vuelta del for la variable elemento 
almacena un valor de la lista.

Problema propuesto 1:

Definir una función que cargue una lista con palabras y la retorne.
Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.
"""

def cargar(r=5):
	palabras = []
	for x in range(r):
		p = input("Palabra: ")
		palabras.append(p)
	return palabras

def mostrar(palabras):
	for p in palabras:
		size = len(p)
		if size > 5:
			print("La palabra '",p,"' tiene '",size, "' caracteres.", sep="")

palabras = cargar()
mostrar(palabras)