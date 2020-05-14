"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. 
Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""

nombres = []
edades = []

for x in range(5):
	n = input("Inserte el nombre: ")
	nombres.append(n)
	e = int(input("Inserte edad: "))
	edades.append(e)

for x in range(5):
	if edades[x] >= 18:
		print("Nombre:",nombres[x], "- Edad:",edades[x])