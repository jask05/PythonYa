x = 1
cantidad = 0
n = int(input("Numero de piezas:"))
while x <= n:
    largo = float(input("Largo de la pieza en cm (puede utilizar puntos):"))
    if largo >= 1.20 and largo <= 1.30:
        cantidad = cantidad + 1
    x = x + 1
print("Numero de piezas aptas: ")
print(cantidad)