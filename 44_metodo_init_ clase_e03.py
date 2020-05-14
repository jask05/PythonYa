"""
Problema propuesto

Desarrollar una clase que represente un Cuadrado y tenga los siguientes métodos: inicializar el valor
del lado llegando como parámetro al método __init__ (definir un atributo llamado lado), imprimir su
perímetro y su superficie.
"""

class Cuadrado:

    def __init__(self):
        self.cuadrado = int(input("Lado del cuadrado: "))

    def perimetro(self):
        return self.cuadrado * 4

    def superficie(self):
        return self.cuadrado * self.cuadrado

c = Cuadrado()
print("Perímetro: ",c.perimetro())
print("Superficie: ",c.superficie())