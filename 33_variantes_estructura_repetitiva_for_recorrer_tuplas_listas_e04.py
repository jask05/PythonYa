"""
lista=[2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)

Como podemos ver la instrucción for requiere una variable (en este ejemplo llamada elemento), 
luego la palabra clave in y por último el nombre de la lista. El bloque del for se ejecuta 
tantas veces como elementos tenga la lista, y en cada vuelta del for la variable elemento 
almacena un valor de la lista.

Problema propuesto 2:

Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""
def cargar(r=5):
	productos = []
	for x in range(r):
		n = input("Nombre del producto: ")
		p = int(input("Precio del producto: "))
		productos.append((n,p))

	return productos

def listar(productos):
	for producto,precio in productos:
		print("El producto '",producto,"' tiene un precio de '",precio,"' euros.")

def filtro(productos):
	for producto,precio in productos:
		if precio >= 10 and precio <=15:
			print(producto," con precio: ",precio)			

compra = cargar()
listar(compra)
print("=== Productos entre 10 y 15€ ===")
filtro(compra)