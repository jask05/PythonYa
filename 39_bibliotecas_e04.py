"""
Confeccionar una programa con las siguientes funciones:
1) Generar una lista con 5 elementos enteros aleatorios comprendidos entre 1 y 3.
2) Controlar que el primer elemento de la lista sea un 1, en el caso que haya un 2 o 3 mezclar la lista y volver a controlar hasta que haya un 1.
3) Imprimir la lista.
"""

import random

def genrandom(v1=5):
    lista = []
    x = 0
    while x < v1:
        num = random.randint(1,3)
        lista.append(num)
        x = x + 1

    return lista

def control(lista):
    if 1 in lista:
        if lista[0] != 1:
            while lista[0] != 1:
                random.shuffle(lista)
        if lista[0] == 1:
            print(lista)
    else:
        print("No hay un 1 en la lista.")

numeros = genrandom()
control(numeros)