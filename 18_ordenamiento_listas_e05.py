"""
Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla, luego ordenar de mayor a menor e imprimir nuevamente.
"""

e = []
for x in range(5):
	i = int(input("Numero: "))
	e.append(i)

u = e
t1 = ""
t2 = ""

# Menor a mayor
for k in range(4):
	for x in range(4-k):
		if e[x] > e[x+1]:
			t1 = e[x+1]
			e[x+1] = e[x]
			e[x] = t1

print("Ordenado de menor a mayor: ", e)

# Mayor a menor
for k in range(4):
	for x in range(4-k):
		if u[x] < u[x+1]:
			t1 = u[x]
			u[x] = u[x+1]
			u[x+1] = t1

print("Ordenado de mayor a menor: ", u)