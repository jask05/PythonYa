"""
productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)

Para consultar si una clave se encuentra en el diccionario podemos utilizar el operador in:
if clave in diccionario:
    print(diccionario[clave])

Problema 2:

Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos 
y como valor el precio del mismo.
Desarrollar además las funciones de:
1) Imprimir en forma completa el diccionario
2) Imprimir solo los artículos con precio superior a 100.
"""

def cargar():
    productos={}
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:"))
        productos[nombre]=precio
    return productos


def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])


def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre]>100:
            print(nombre)

            
# bloque principal

productos=cargar()
imprimir(productos)
imprimir_mayor100(productos)