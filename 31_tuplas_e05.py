"""
Una vez inicializada la tupla no podemos agregar, borrar o modificar sus elementos.
Utilizamos una tupla para agrupar datos que por su naturaleza están relacionados y que no serán modificados durante la ejecución del programa.

Confeccionar un programa con las siguientes funciones:
1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados 
y muestre el nombre del empleado con sueldo mayor.
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente 
llamar a la función que muestra el nombre de empleado con sueldo mayor.
# bloque principal

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)
"""

def cargar():
	nombre = input("Nombre del empleado: ")
	sueldo = int(input("Sueldo: "))
	return (nombre, sueldo)

def mayor_sueldo(e1,e2):
	nombre_mayor = ""
	if e1[1] > e2[1]:
		nombre_mayor = e1[0]
	elif e1[1] < e2[1]:
		nombre_mayor = e2[0]

	return nombre_mayor

e1 = cargar()
e2 = cargar()
print("Primer empleado: ",e1)
print("Segundo empleado: ", e2)
mayor = mayor_sueldo(e1,e2)
print("Nombre del empleado que cobra más: ", mayor)