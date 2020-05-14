"""
Desarrollar un programa que solicite la carga de tres valores y muestre el menor. 
Desde el bloque principal del programa llamar 2 veces a dicha función 
(sin utilizar una estructura repetitiva)
"""

def menor():
    v1 = int(input("Valor 1: "))
    v2 = int(input("Valor 2: "))
    v3 = int(input("Valor 3: "))

    minus = 0
    if v1 < v2 and v1 < v3:
        minus = v1
    elif v2 < v3:
        minus = v2
    else:
        minus = v3

    print("El valor más pequeño es: ",minus)

for x in range(2):
    menor()
    print("---------------------")