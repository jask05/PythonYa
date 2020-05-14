"""
Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
c - Calcular la temperatura media trimestral de cada país.
c - Imprimr los nombres de los paises y las temperaturas medias trimestrales.
b - Imprimir el nombre del pais con la temperatura media trimestral mayor.
Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días.
Desarrollar un programa que cree una lista de 50 elementos. El primer elemento es una lista con un elemento entero, el segundo elemento es una lista de dos elementos etc.
La lista debería tener esta estructura y asignarle esos valores a medida que se crean los elementos:
[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], etc....]
"""

pais = ""
paises = []

temp = ""
temps = []

suma = 0
tempmedia = []



# Pais y tres temperaturas
for x in range(3):
    pais = input("### Inserte pais: ")
    paises.append(pais)
    temps.append([])
    for k in range(3):
        temp = int(input("> Temperatura: "))
        temps[x].append(temp)

# Media de temperaturas
for m in range(3):
    tamanio = len(temps[m])
    for s in range(tamanio):
        suma = suma + temps[m][s]

    tempmedia.append(suma/tamanio)

# Temp media mas alta


print("Paises: ",paises)
print("Temperaturas: ", temps)
print("Temperaturas medias: ",tempmedia)