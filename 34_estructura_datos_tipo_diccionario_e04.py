"""
productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)

Para consultar si una clave se encuentra en el diccionario podemos utilizar el operador in:
if clave in diccionario:
    print(diccionario[clave])

Problema propuesto

Crear un diccionario en Python que defina como clave el número de documento de una persona y 
como valor un string con su nombre.
Desarrollar las siguientes funciones:
1) Cargar por teclado los datos de 4 personas.
2) Listado completo del diccionario.
3) Consulta del nombre de una persona ingresando su número de documento.
"""

def cargar():
	continuar = "s"
	documentos = {}
	while continuar=="s":
		n = int(input("Documento: "))
		p = input("Nombre: ")
		documentos[n] = p
		continuar = input("¿Deseas añadir un registro nuevo? [s/n]")

	return documentos

def listado_completo(documentos):
	for documento in documentos:
		print("El documento '",documento,"' pertenece a '",documentos[documento],"'")

def filtro(documentos):
	continuar = "s"
	while continuar == "s":
		filtrar = int(input("Inserte el documento por el que quiere buscar: "))
		if filtrar in documentos:
			print("Existe la persona '",filtrar,"'.")
		else:
			print("No existe la persona que busca.")

		continuar = input("¿Desea realizar otra búsqueda? [s/n]")

documentos = cargar()
listado_completo(documentos)
filtro(documentos)