"""
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales. 
Llamarla desde el bloque principal del programa 3 veces con string distintos.
"""

def vocales(str):
    size = len(str)
    count = 0
    for x in range(size):
        if str[x].lower() == "a" or str[x].lower() == "e" or str[x].lower() == "i" or str[x].lower() == "o" or str[x].lower() == "u":
            count = count + 1

    rs(count) 

def rs(valor):
    print("------------------------")
    print("Tienes: ",valor,"vocales.")
    print("------------------------")

x = 1
while x <= 3:
    v = input("Inserte frase o palabra: ")
    vocales(v)
    x = x + 1