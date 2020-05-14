"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.
"""

def perimetro_cuadrado(lado):
    return lado*4

valor = int(input("Lado: "))
print("El perimetro del cudrado es:",perimetro_cuadrado(valor))