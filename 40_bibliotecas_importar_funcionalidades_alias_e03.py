"""
from random import randint
from random import randint,shuffle
valor=randint(1,10)
print(valor)

Definición de alias para una funcionalidad

Podemos definir un nombre distinto para una funcionalidad que importamos de otro módulo.
Esto puede tener como objetivo que nuestro programa sea más legible o evitar que un nombre
de función que importamos colisione con un nombre de función de nuestro propio módulo.
Resolveremos el mismo problema anterior pero definiendo dos alias para las funciones sqrt y pow del módulo math.

Problema propuesto

Calcular el factorial de un número ingresado por teclado.
El factorial de un número es la cantidad que resulta de la multiplicación de determinado número natural por todos los
números naturales que le anteceden excluyendo el cero. Por ejemplo el factorial de 4 es 24,
que resulta de multiplicar 4*3*2*1.
No hay que implementar el algoritmo para calcular el factorial sino hay que importar dicha funcionalidad del módulo math.
El módulo math tiene una función llamada factorial que recibe como parámetro un entero del que necesitamos que
nos retorne el factorial.
Solo importar la funcionalidad factorial del módulo math de la biblioteca estándar de Python.
"""

from math import factorial as f

def calcularFactorial():
    num = int(input("Inserte un número mayor de 0: "))
    if num > 0:
        return f(num)

print(calcularFactorial())