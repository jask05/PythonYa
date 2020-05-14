"""
Problemas propuestos

Confeccionar un programa que genere un número aleatorio entre 1 y 100 y no se muestre.
El operador debe tratar de adivinar el número ingresado.
Cada vez que ingrese un número mostrar un mensaje "Gano" si es igual al generado o "El número aleatorio el mayor" o "El número aleatorio es menor".
Mostrar cuando gana el jugador cuantos intentos necesitó.
"""

import random

def aleatorio(v1=1,v2=10):
    num = random.randint(v1,v2)
    return num

def adivinar(num):
    continuar = "s"
    while continuar == "s":
        check = int(input("Escoja un número: "))
        if check == num:
            print("Ganó!")
            continuar = "n"
        elif check > num:
            print("Siga intentando. El número aleatorio es más pequeño.")
        elif check < num:
            print("Siga intentando. El número aleatorio es más grande.")

num = aleatorio()
adivinar(num)