"""
Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos
(lo que conocemos como funciones).

La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá
sus propios valores y compartirán las mismas funciones.

self:
sirve para referirse al objeto actual. Este mecanismo es necesario para
poder acceder a los atributos y métodos del objeto diferenciando, por ejemplo, una variable local mi_var
de un atributo del objeto self.mi_var.

Problema 2:

Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para
inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
Definir dos objetos de la clase Alumno.
"""

class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal

alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()
