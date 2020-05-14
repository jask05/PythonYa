"""
Problema propuesto

Desarrollar un programa que implemente una clase llamada Jugador.
Definir como atributos su nombre y puntaje.
Codificar el método especial __str__ que retorne el nombre y si 
es principiante (menos de 1000 puntos) o experto (1000 o más puntos)
"""

class Jugador:

    def __init__(self,nombre,puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def __str__(self):
        cadena=self.nombre+" es "
        if self.puntuacion < 1000:
            cadena=cadena+"principiante"
        else:
            cadena=cadena+"experto"
        return cadena

j1=Jugador("Agustin",100)
j2=Jugador("Blanca",10000)
print(j1)
print(j2)