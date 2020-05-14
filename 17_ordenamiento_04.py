"""
Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una.
Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista.
Mostrar esta tercer lista.
"""
l1 = []
l2 = []
l3 = []

for x in range(4):
	n1 = int(input("(1) Ingrese número: "))
	l1.append(n1)
	n2 = int(input("(2) Ingrese número: "))
	l2.append(n2)

for x in range(4):
	l3.append(l1[x]+l2[x])

print(l1)
print(l2)
print(l3)