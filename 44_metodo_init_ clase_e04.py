"""
Problema propuesto

Implementar la clase Operaciones. Se deben cargar dos valores enteros por teclado en el método __init__,
calcular su suma, resta, multiplicación y división, cada una en un método, imprimir dichos resultados.
"""

class Operaciones:

    def __init__(self):
        self.v1 = int(input("Valor 1: "))
        self.v2 = int(input("Valor 2: "))

    def suma(self):
        print("Suma:", self.v1 + self.v2)

    def resta(self):
        print("Resta:", self.v1 - self.v2)

    def multiplicacion(self):
        print("Multiplicación:", self.v1 * self.v2)

    def division(self):
        print("División:", self.v1 / self.v2)

o1 = Operaciones()
o1.suma()
o1.resta()
o1.multiplicacion()
o1.division()
