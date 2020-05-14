x = 1
mayores = 0
menores = 0

while x <= 10:
    notas = int(input("Notas: "))
    if notas < 7:
        menores = menores + 1
    else:
        mayores = mayores + 1

    x = x +1

print("Notas menores de 7: ")
print(menores)
print("Notas mayores de 7: ")
print(mayores)