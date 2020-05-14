"""
Problema propuesto

Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de legajo y en su valor almacenar 
una lista con el nombre, profesión y sueldo.
Desarrollar las siguientes funciones:
1) Carga de datos de empleados.
2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.
3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"
"""

def cargar():
    empleados = {}
    continuar = "s"
    while continuar == "s":
        id = int(input("Inserte identificación de empleado (numérica): "))
        lista = []
        nombre = input("Nombre: ")
        profesion = input("Profesión: ")
        sueldo = int(input("Sueldo:"))
        lista.append(nombre)
        lista.append(profesion)
        lista.append(sueldo)
        empleados[id]=lista
        continuar = input("¿Desea añadir otro empleado? [s/n] ")

    return empleados

def modificar_sueldo(empleados):
    modificar = input("¿Desea modificar el sueldo de algún empleado? [s/n]")
    if modificar == "s":
        id = int(input("Identificación del empleado a buscar: "))
        continuar = "s"
        while continuar == "s":
            if id in empleados:
                print("== Datos del empleado == ")
                print("Nombre: ",empleados[id][0])
                print("Profesión: ",empleados[id][1])
                print("Sueldo: ",empleados[id][2])
                print("========")
                nuevosueldo = int(input("Introduzca la cantidad que desea añadir: "))
                empleados[id][2] = nuevosueldo
                print("Nuevo sueldo: ",empleados[id][2])
            else:
                print("No se encuentra ningún empleado con esa identificación.")

            continuar = input("¿Desea buscar y/o modificar el sueldo de otro empleado? [s/n] ")

def filtro(empleados):
    for id in empleados:
        empleado = empleados[id][1].lower()
        if empleado == "analista de sistemas":
            print("== Datos de empleados == ")
            print("Nombre: ",empleados[id][0])
            print("Profesión: ",empleados[id][1])
            print("Sueldo: ",empleados[id][2])
            print("========")

empleados = cargar()
modificar_sueldo(empleados)
filtro(empleados)