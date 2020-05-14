"""
Problema propuesto

Se desea almacenar los datos de 3 alumnos. 
Definir un diccionario cuya clave sea el número de documento del alumno. 
Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.
"""

def cargar():
	alumnos = {}
	continuar = "s"
	while continuar == "s":
		continuar2 = "s"
		dni = int(input("DNI: "))
		lista = []
		while continuar2 == "s":
			materia = input("Materia: ")
			nota = float(input("Nota: "))
			lista.append((materia,nota))
			continuar2 = input("¿Desea introducir un nuevo registro (materia/nota)? [s/n]")
		alumnos[dni]=lista
		continuar = input("¿Desea insertar otro alumno? [s/n] ")
	return alumnos

def listado(alumnos):
	for alumno in alumnos:
		print("DNI: ",alumnos[alumno])
		for materia,nota in alumnos[alumno]:
			print("Materia: ",materia)
			print("Nota: ",nota)

def filtro(alumnos):
	continuar = "s"
	while continuar == "s":
		dni = int(input("Inserte el DNI por el que quiere buscar: "))
		if dni in alumnos:
			for materia,nota in alumnos[dni]:
				print("=> Materia: ",materia)
				print("=> Nota: ",nota)
		else:
			print("El alumno que busca NO existe en nuestra base de datos.")
		continuar = "¿Desea realizar otra búsqueda? [s/n] "


alumnos = cargar()
listado(alumnos)
filtro(alumnos)