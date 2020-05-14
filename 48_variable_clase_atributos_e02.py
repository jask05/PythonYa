"""
Problema propuesto

Plantear una clase llamada Jugador.
Definir en la clase Jugador los atributos nombre y puntaje, y los métodos __init__,
imprimir y pasar_tiempo (que debe reducir en uno la variable de clase).
Declarar dentro de la clase Jugador una variable de clase que indique
cuantos minutos falta para el fin de juego (iniciarla con el valor 30)
Definir en el bloque principal dos objetos de la clase Jugador.
Reducir dicha variable hasta llegar a cero.
"""

class Jugador:

    tiempo = 30

    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print("El jugador '",self.nombre,"' tiene una puntuación de '",self.puntaje,"'", sep="")

    def pasar_tiempo(self):
        print("==> El juego termina en ",Jugador.tiempo," minutos.", sep="")
        Jugador.tiempo = Jugador.tiempo-1

j1 = Jugador("Agus",2000)
j2 = Jugador("Blanca", 4000)
while Jugador.tiempo > 0:
    j1.imprimir()
    j2.imprimir()
    j1.pasar_tiempo()
