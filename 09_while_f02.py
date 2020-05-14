n = 1
x = int(input("¿Cuantas alturas vas a ingresar? "))
suma = 0
while n <= x:
    altura = int(input("Alturas: "))
    suma = suma + altura
    n = n + 1

media = suma / x
print("Media de alturas: ")
print(media)