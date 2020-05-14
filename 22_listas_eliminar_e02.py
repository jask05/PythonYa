"""
Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

Para eliminar elementos de una lista también es empleada la función "del" pasando como parámetro la referencia de la componente a eliminar:
lista=[10, 20, 30, 40, 50]

print(lista)

del(lista[0])
del(lista[1])
del(lista[2])

print(lista)
"""

lista=[]
for x in range(10):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

print(lista)

posicion=0
while posicion<len(lista):
    if lista[posicion]==5:
        lista.pop(posicion)
    else:
        posicion=posicion+1
    
print(lista)  