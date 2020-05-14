"""
Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una
lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas.
Imprimir luego cada nombre y sus dos notas.
"""

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]

print(lista)

for x in range(len(lista[0])):
	if lista[0][x] > 50:
		lista[0][x] = 0

print(lista)
print("-------------------------------------")
lista2=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]

"""
Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 10 contenidos 
en todos los elementos de la variable "lista". Volver a imprimir la lista.
"""

print(lista2)

for k in range(len(lista2)):
	for x in range(len(lista2[k])):
		if lista2[k][x] > 10:
			lista2[k][x] = 0

print(lista2)

"""
Crear una lista por asignación con la cantidad de elementos de tipo lista que usted desee. 
Luego imprimir el último elemento de la lista principal.
"""
lista3=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
size = len(lista3)
print(lista3[size-1])