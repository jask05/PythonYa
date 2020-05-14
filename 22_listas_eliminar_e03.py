"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""

nombres = ["Agus", "Blanca", "Oscar", "Chiara", "Gian", "Lili", "Dani", "Iván", "Marina", "Manu"]
sueldos = [20000, 15000, 10000, 5000, 250, 2300, 11000, 9000, 400, 1050]

print(nombres)
print(sueldos)

count = 0
while count < len(sueldos):
    if sueldos[count] > 10000:
        sueldos.pop(count)
        nombres.pop(count)
    else:
        count = count + 1

print("--------------------")
print(nombres)
print(sueldos)