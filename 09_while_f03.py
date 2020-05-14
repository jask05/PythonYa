x = 1
sueldo = 0
empleados = int(input("Numero de empleados: "))
entre100y300 = 0
masde300 = 0
sueldototal = 0
while x <= empleados:
    sueldo = int(input("Sueldo: "))

    sueldototal = sueldototal + sueldo
    if sueldo >= 100 and sueldo <= 300:
        entre100y300 = entre100y300 + 1
    elif sueldo > 300:
        masde300 = masde300 + 1

    x = x + 1

print("Sueldo total gastado: ")
print(sueldototal)
print("Cobran entre 100 y 300: ")
print(entre100y300)
print("Cobran mas de 300: ")
print(masde300)