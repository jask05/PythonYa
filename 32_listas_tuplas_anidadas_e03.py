"""
La lista es una estructura mutable (es decir podemos modificar sus elementos, agregar y borrar) 
en cambio una tupla es una secuencia de datos inmutable, es decir una vez definida no puede 
cambiar.

Almacenar en una lista de 5 elementos los nombres de empleados de una empresa junto 
a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 
en los últimos tres meses.
"""

def almacena(v=5):
	currantes = []
	for x in range(v):
		nombre = input("Nombre del empleado: ")
		s1 = int(input("Primer sueldo: "))
		s2 = int(input("Segundo sueldo: "))
		s3 = int(input("Tercer sueldo: "))

		currantes.append((nombre,s1,s2,s3))

	return currantes

def total_cobrado(empleados):
	total = []
	empleado = []
	# Primero saber cuántas listas hay
	for x in range(len(empleados)):
		suma = 0
		# Obtener los sueldos
		for y in range(1,len(empleados[x])):
			suma = suma + empleados[x][y]

		empleado.append(empleados[x][0])
		total.append(suma)

	return empleado,total

def ingreso_mayor(empleado,total):
	nombres = []
	for x in range(len(empleado)):
		if total[x] > 10000:
			nombres.append(empleado[x])

	return nombres

def imprimir(empleado,total):
	for x in range(len(empleado)):
		print("El empleado: ",empleado[x], " ha cobrado un total de: ",total[x],"€", sep="")

currantes = []
currantes.append(("A",100,1001,1002))
currantes.append(("B",2200,200,2400))
currantes.append(("C",3300,3400,3500))
currantes.append(("D",1,1,1))
currantes.append(("E",5500,560,570))
empleado,total = total_cobrado(currantes)
imprimir(empleado,total)
print("Empleados que superaron los 10.000€: ",ingreso_mayor(empleado,total))