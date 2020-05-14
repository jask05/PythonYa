datos = int(input("Num. de datos a ingresar: "))
mayor12 = 0
for f in range(datos):
    print("==========> OCURRENCIA: ", f + 1)
    base = int(input("Base: "))
    altura = int(input("Altura: "))
    resultado = (base*altura)/2
    print("Base: ",base)
    print("Altura: ",altura)
    print("Superficie: ",resultado)
    if resultado > mayor12:
        mayor12 = mayor12 + 1

print("Triangulos cuya superficie es mayor a 12: ",mayor12)