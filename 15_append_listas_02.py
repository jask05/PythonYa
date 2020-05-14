# Problema 02: Realizar la carga de valores enteros por teclado, almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

lista = []
c = 1
while c != 0:
	c = int(input("Valor: "))
	lista.append(c)

print(lista)