"""
Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más posiciones en la lista)
"""

nombre = []

for x in range(5):
    p = input("Nombre persona: ")
    nombre.append(p)

menor = nombre[0]

for x in range(1,5):
    if nombre[x] < menor:
        menor = nombre[x]

print("Nombres: ", nombre)
print("Menor: ",menor)