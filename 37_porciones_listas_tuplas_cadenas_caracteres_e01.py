"""
El lenguaje Python nos facilita una sintaxis muy sencilla par recuperar un trozo de una lista, tupla o cadena de caracteres.

lista1=[0,1,2,3,4,5,6]
# Para recuperar una "porción" o trozo de una lista debemos indicar en el subíndice dos valores separados por el caracter ":".
# Del lado izquierdo indicamos a partir de que elementos queremos recuperar y del lado derecho hasta cual posición sin incluir dicho valor.
lista2=lista1[2:5] 
print(lista2) # 2,3,4
lista3=lista1[1:3]
print(lista3) # 1,2
lista4=lista1[:3]
print(lista4) # 0,1,2
lista5=lista1[2:]
print(lista5) # 2,3,4,5,6

Problema 1:

Confeccionar una función que le enviemos un número de mes como parámetro y nos 
retorne una tupla con todos los nombres de meses que faltan hasta fin de año.
"""

def meses_faltantes(numeromes):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numeromes:]


# bloque principal

print("Imprimir los nombres de meses que faltan hasta fin de año")
numeromes=int(input("Ingrese el numero de mes:"))
mesesfalta=meses_faltantes(numeromes)
print(mesesfalta)