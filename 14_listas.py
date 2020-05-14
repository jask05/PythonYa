# Problema 01: Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
lista = [33, 56, 89, 98, 101]
x = 0
suma = 0

while x < len(lista):
	suma = suma + lista[x]
	x = x + 1

print("Suma:", suma)