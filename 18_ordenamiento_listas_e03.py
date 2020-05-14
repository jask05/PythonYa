"""
Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla.
"""

paises = []
temp = ""

for x in range(5):
	pais = input("País: ")
	paises.append(pais)

print("Paises sin ordenar: ",paises)

for k in range(4):
	for x in range(4-k):
		if paises[x] > paises[x+1]:
			temp = paises[x+1]
			paises[x+1] = paises[x]
			paises[x] = temp

print("Paises ordenados: ", paises)