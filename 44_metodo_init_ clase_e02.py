"""
Problema 2:

Desarrollar una clase que represente un punto en el plano y tenga los siguientes métodos: inicializar los valores
de x e y que llegan como parámetros, imprimir en que cuadrante se encuentra dicho punto
(concepto matemático, primer cuadrante si x e y son positivas, si x<0 e y>0 segundo cuadrante, etc.)
"""

class Punto:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def imprimir(self):
        print("Coordenada del punto")
        print("(",self.x,",",self.y,")")

    def imprimir_cuadrante(self):
        if self.x>0 and self.y>0:
            print("Primer cuadrange")
        else:
            if self.x<0 and self.y>0:
                print("Segundo cuadrante")
            else:
                if self.x<0 and self.y<0:
                    print("Tercer cuadrante")
                else:
                    if self.x>0 and self.y<0:
                        print("Cuarto cuadrante")


# bloque principal

punto1=Punto(10,-2)
punto1.imprimir()
punto1.imprimir_cuadrante()

punto2=Punto(-10,-2)
punto2.imprimir()
punto2.imprimir_cuadrante()

punto3=Punto(-10,2)
punto3.imprimir()
punto3.imprimir_cuadrante()

punto4=Punto(10,2)
punto4.imprimir()
punto4.imprimir_cuadrante()