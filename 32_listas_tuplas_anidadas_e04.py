"""
La lista es una estructura mutable (es decir podemos modificar sus elementos, agregar y borrar) 
en cambio una tupla es una secuencia de datos inmutable, es decir una vez definida no puede 
cambiar.

Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla 
con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
candidatos=[("juan", [("cordoba",100),("buenos aires",200]]), ("ana", [("cordoba",55)]]), ("luis", [("buenos aires",20]])]
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.
"""

def candidato():
	nombre = input("Nombre del candidato: ")
	return nombre

def ciudad_voto():
	ciudad = input("Nombre de la ciudad: ")
	voto = int(input("Voto: "))
	return (ciudad,voto)

def resumen(n=3,cv=2):
	candidatos = []
	# Se controla la insercción de nombres
	for x in range(n):
		nombre = candidato()
		candidatos.append(nombre)
		# Se controla la insercción de votos y ciudades
		votos = []
		for y in range(cv):
			c_v = ciudad_voto()
			votos.append(c_v)

		candidatos.append(votos)

	return candidatos

def votos_totales(resumen):
	candidatos = []
	resultados = []
	for x in range(len(resumen)):
		# > 1 porque hay mix de valores fijos y listas
		suma = 0
		if len(resumen[x]) > 1:
			for y in range(len(resumen[x])):
				suma = suma + resumen[x][y][1]
			resultados.append(suma)
		else:
			candidatos.append(resumen[x])

	return candidatos,resultados

def print_bien(candidatos,votos):
	for x in range(len(candidatos)):
		print("El candidato '",candidatos[x],"' ha obtenido '",votos[x],"' votos.", sep="")

# resumen = resumen()
resumen = ['A', [('a', 12), ('b', 55)], 'B', [('c', 88), ('d', 9)], 'C', [('e', 44), ('f', 1)]]
# print(resumen)
candidatos, votos = votos_totales(resumen)
print_bien(candidatos,votos)