"""
Elaborar una función que muestre la tabla de multiplicar del valor que le enviemos como parámetro. 
Definir un segundo parámetro llamado termino que por defecto almacene el valor 10. 
Se deben mostrar tantos términos de la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con argumentos nombrados.
"""

def multiplicar(valor,termino=10):
	if termino > 0:
		for x in range(termino):
			m = x+1
			print(valor,"x",m,"=",valor*m)

multiplicar(termino=10,valor=2)