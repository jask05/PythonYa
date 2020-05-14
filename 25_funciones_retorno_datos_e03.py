"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos
"""

def promedio(e1, e2, e3):
    rs = e1 + e2 + e3
    return rs / 3

v1 = int(input("Ingrese el valor 1: "))
v2 = int(input("Ingrese el valor 2: "))
v3 = int(input("Ingrese el valor 3: "))

print("El valor promedio es:",promedio(v1,v2,v3))