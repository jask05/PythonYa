# Problema 01: Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista. Imprimir la lista generada.

lista = []
x = 0
i = 5
while x < i:
	v = int(input("Introduce un valor numérico: "))
	lista.append(v)
	x = x + 1
print(lista)