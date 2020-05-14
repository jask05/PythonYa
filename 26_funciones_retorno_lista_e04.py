"""
Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
"""

def mascaracteres(palabras):
    mas = palabras[0]
    for x in range(1,len(palabras)-1):
        if len(mas) < len(palabras[x]):
            mas = palabras[x]

    return mas

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))