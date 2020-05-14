"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes 
(de mayor a menor) e imprimir nuevamente.
"""

paises = []
habitantes = []

for x in range(5):
	pais = input("Introduzca el nombre de un país: ")
	paises.append(pais)
	habitante = int(input("Nº de habitantes: "))
	habitantes.append(habitante)

t1 = ""
t2 = ""
h2 = habitantes
p2 = paises

for k in range(4):
	for x in range(4-k):
		if paises[x] > paises[x+1]:
			t1 = paises[x]
			paises[x] = paises[x+1]
			paises[x+1] = t1

			t2 = habitantes[x]
			habitantes[x] = habitantes[x+1]
			habitantes[x+1] = t2

print(paises,habitantes)

t3 = ""
t4 = ""

for y in range(4):
	for z in range(4-y):
		if h2[z] < h2[z+1]:
			t3 = h2[z]
			h2[z] = h2[z+1]
			h2[z+1] = t3

			t4 = p2[z]
			p2[z] = p2[z+1]
			p2[z+1] = t4

print(p2, h2)