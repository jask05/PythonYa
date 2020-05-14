"""
Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear y cargar una lista con todos los sueldos de dichos empleados. Imprimir la lista de sueldos.
"""

empleados = int(input("Número de empleados: "))

sueldos = []
for x in range(empleados):
	sueldo = int(input("Sueldo: "))
	sueldos.append(sueldo)

print("Sueldo de todos los empleados: ",sueldos)