"""
Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos debe retornar la suma de dichos valores. 
Debe tener tres parámetros por defecto.
"""

def enteros(e1, e2, e3=10, e4=20, e5=30):
    suma = e1 + e2 + e3 + e4 + e5
    return suma

print(enteros(20,50))
print(enteros(20,50,80,901,101))