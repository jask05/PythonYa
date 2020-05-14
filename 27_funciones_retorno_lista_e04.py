"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
3) Retornar el promedio de los sueldos.
4) Mostrar todos los sueldos que están por debajo del promedio.
"""

def imprime_sueldos(sueldos):
    mayorque = 0
    menorque = []
    suma = 0
    for x in range(len(sueldos)):

        suma = suma + sueldos[x]

        if sueldos[x] > 4000:
            mayorque = mayorque + 1

    promedio = suma // len(sueldos)

    for y in range(len(sueldos)):
        if promedio > sueldos[y]:
            menorque.append(sueldos[y])

    return mayorque,promedio,menorque

sueldos = [4000, 5000, 3000, 1000, 10000]
mayor,promedio,menor = imprime_sueldos(sueldos)
print("Hay",mayor,"sueldos mayores a 4000. El promedio es:",promedio)
print("Sueldos menores que el promedio:",menor)