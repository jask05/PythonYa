"""
Una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos.
Utilizamos una tupla para agrupar datos que por su naturaleza están relacionados y que no serán modificados durante la ejecución del programa.

Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.
"""

def carga():
	lista = []
	for x in range(5):
		y = int(input("Valor: "))
		lista.append(y)

	return lista

def mayor(valor):
	max = valor[0]
	min = valor[0]
	for x in range(1,len(valor)):
		if valor[x] > max:
			max = valor[x]
		elif valor[x] < min:
			min = valor[x]

	return (max,min)

valores = carga()
maxmin = mayor(valores)
print("Devuelto como tupla: ",maxmin)
lista = list(maxmin)
print("Devuelto como lista: ",lista)