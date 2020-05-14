"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. Definir dos listas paralelas. 
Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.
"""

productos = []
precios = []

for x in range(5):
	p = input("Producto: ")
	productos.append(p)
	c = int(input("Precio producto: "))
	precios.append(c)
	print("--------------------------")

count = 0
mayor = precios[0]
for x in range(1,5):
	if precios[x] > mayor:
		count = count + 1

print("Hay",count," producto(s) más caros que el primero: ", productos[0],"->",precios[0])