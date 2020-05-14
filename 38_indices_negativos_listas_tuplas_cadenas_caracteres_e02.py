"""
Problemas propuestos

Cargar una cadena de caracteres por teclado. Mostrar la cadena del final al principio 
utilizando subíndices negativos.
Confeccionar un programa con las siguientes funciones:
1) Cargar una lista con 5 palabras.
2) Intercambiar la primer palabra con la última.
3) Imprimir la lista
"""

def cargar(palabras):
    print(palabras)
    size = len(palabras)
    ulti = palabras[size-1]
    palabras[size-1] = palabras[0]
    palabras[0] = ulti
    print(palabras)

lista = ["hola", "esto", "es", "una", "prueba"]
cargar(lista)