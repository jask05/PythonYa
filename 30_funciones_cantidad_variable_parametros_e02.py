"""
Confeccionar una función que reciba una serie de edades y me retorne la cantidad que 
son mayores o iguales a 18 (como mínimo se envía un entero a la función)
"""

def edades(v1,*v2):
	mayores = 0
	if v1 >= 18:
		mayores = mayores + 1

	for x in range(len(v2)):
		if v2[x] >= 18:
			mayores = mayores + 1

	return mayores

print("Mayores de 18 años")
print(edades(12,13,14,15,18,19,20,22,12,51,32))