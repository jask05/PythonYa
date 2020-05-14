"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
"""

def cantidad_letras(valor):
    tamanio = len(valor)
    x = 0
    y = 0
    z = 0

    while x < tamanio:
        if valor[x] == "a":
            y = y + 1
        elif valor[x] == "A":
            z = z +1
        x = x + 1

    rs = [y,z]
    return rs

v = input("Introduzca una frase: ")
rs = cantidad_letras(v)
print("La frase tiene: ",rs[0], "letras a minusculas y ", rs[1], "letras A mayusculas.")