"""
Problema 1:

Definir una clase llamada Punto con dos atributos x e y.
Crearle el método especial __str__ para retornar un string con el formato (x,y).
"""

class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"


# bloque principal

punto1=Punto(10,3)
punto2=Punto(3,4)
print(punto1)
print(punto2)