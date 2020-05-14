"""
Definir una lista de enteros por asignación en el bloque principal.
Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos.
Mostrar dicho producto en el bloque principal de nuestro programa.
"""

def producto(valor):
    x = 0
    rs = 1
    while x <= len(valor)-1:
        rs = rs * valor[x]
        x = x + 1

    return rs

valor = [1,2,3]
print(producto(valor))