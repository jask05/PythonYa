"""
Problemas propuestos

Realizar un programa que contenga las siguientes funciones:
1) Carga de una lista de 10 enteros.
2) Recibir una lista y retornar otra con la primer mitad (se sabe que siempre llega una lista con una cantidad par de elementos)
3) Imprimir una lista.

Cargar una cadena por teclado luego:
1) Imprimir los dos primeros caracteres.
2) Imprimir los dos últimos
3) Imprimir todos menos el primero y el último caracter.
"""

def cargar():
    lista = []
    for x in range(10):
        e = int(input("Entero: "))
        lista.append(e)
    return lista

def cargar_texto():
    lista = []
    for x in range(10):
        t = input("Texto: ")
        lista.append(t)
    return lista

def primera_mitad(lista):
    mitad = len(lista)//2
    return lista[:mitad]

def imprimir(lista):
    print("= Contenido de la lista =")
    print(lista)

def imprimir2primeroschar(lista):
    print("= Imprime los dos primeros caractéres=")
    for x in lista:
        print(x[:2])

def imprimir2ultimoschar(lista):
    print("= Imprime los dos últimos caracteres =")
    for x in lista:
        size = len(x)
        print(x[size-2:size])

def imprimirtodosmenosprimeroyultimo(lista):
    print("= Imprime todos menos el primero y el último caracter =")
    for x in lista:
        size = len(x)
        print(x[1:size-1])

numeros = [1,2,3,4,5,6]
texto = ["artículo","pretendo","explicar","manera","patología","Curvatura","murcielago","ordenador","espalda"]
print("=== Números ===")
print(primera_mitad(numeros))
print(numeros)
print("=== Texto ===")
imprimir(texto)
print(primera_mitad(texto))
imprimir2primeroschar(texto)
imprimir2ultimoschar(texto)
imprimirtodosmenosprimeroyultimo(texto)