"""
Problema 1:

Confeccionar un programa que simule tirar dos dados y luego muestre los valores que salieron. 
Imprimir un mensaje que ganó si la suma de los mismos es igual a 7.
Para resolver este problema requerimos un algoritmo para que se genere un valor aleatorio 
entre 1 y 6. Como la generación de valores aleatorios es un tema muy frecuente la biblioteca 
estándar de Python incluye un módulo que nos resuelve la generación de valores aleatorios.
"""

import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dado:",dado2)
suma=dado1+dado2
if suma==7:
    print("Gano")
else:
    print("Perdio")
    

uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0
siete = 0
ocho = 0
nueve = 0
diez = 0
for x in range(1000):
    dado3 = random.randint(1,10)
    if dado3 == 1:
        uno = uno + 1
    elif dado3 == 2:
        dos = dos + 1
    elif dado3 == 3:
        tres = tres + 1
    elif dado3 == 4:
        cuatro = cuatro + 1
    elif dado3 == 5:
        cinco = cinco + 1
    elif dado3 == 6:
        seis = seis + 1
    elif dado3 == 7:
        siete = siete + 1
    elif dado3 == 8:
        ocho = ocho + 1
    elif dado3 == 9:
        nueve = nueve + 1
    elif dado3 == 10:
        diez = diez + 1

print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(seis)
print(siete)
print(ocho)
print(nueve)
print(diez)