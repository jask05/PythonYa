"""
Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo
parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor
entero enviado.
lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
"""


def multiplicar(lista, valor):
    tamanio = len(lista)-1
    for x in range(tamanio):
        print(lista[x],"x",valor,": ",lista[x]*valor)


lista=[3, 7, 8, 10, 2]
multiplicar(lista,3)
