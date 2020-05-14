"""
Veremos con un ejemplo como podemos pasar como parámetro una lista a una función y posteriormente cambiar su contenido y esto se vea reflejado en la variable que le enviamos al llamarla.
Problema 1:

Confeccionar un programa que contenga las siguientes funciones:
1) Carga de una lista y retorno al bloque principal.
2) Fijar en cero todos los elementos de la lista que tengan un valor menor a 10.
3) Imprimir la lista
"""
def cargar():
    lista=[]
    continua="s"
    while continua=="s":
        valor=int(input("Ingrese un valor:"))
        lista.append(valor)
        continua=input("Agrega otro elemento a la lista[s/n]:")
    return lista


def fijar_cero(li):
    for x in range(len(li)):
        if li[x]<10:
            li[x]=0


def imprimir(lista):
    for elemento in lista:
        print(elemento,"-",sep="",end="")
    print("")

# bloque principal

lista=cargar()
print("Lista antes de modificar")
imprimir(lista)
fijar_cero(lista)
print("Lista despues de modificar")
imprimir(lista)