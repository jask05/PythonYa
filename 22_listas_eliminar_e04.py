"""
Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.
"""

enteros = []
enteros_2 = []

for x in range(5):
    entero = int(input("Inserte número: "))
    enteros.append(entero)

print(enteros)
print("-------------------")

count = 0
while count < len(enteros):
    if enteros[count] >= 10:
        enteros_2.append(enteros[count])
        enteros.pop(count)
    else:
        count = count + 1

print(enteros)
print(enteros_2)