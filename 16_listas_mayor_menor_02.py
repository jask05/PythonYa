lista=[]
for x in range(5):
    valor=int(input("Ingrese valor:"))
    lista.append(valor)

menor=lista[0]
posicion=0
for x in range(1,5):
    print(x)
    if lista[x]<menor:
        menor=lista[x]
        posicion=x

print("Lista completa")
print(lista)
print("Menor de la lista")
print(menor)
print("Posicion del menor en la lista")
print(posicion)