"""
Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos
(lo que conocemos como funciones).

La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá
sus propios valores y compartirán las mismas funciones.

self:
sirve para referirse al objeto actual. Este mecanismo es necesario para
poder acceder a los atributos y métodos del objeto diferenciando, por ejemplo, una variable local mi_var
de un atributo del objeto self.mi_var.

Problema 1:

Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones),
uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
Definir dos objetos de la clase Persona.
"""

class Persona:

    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print("Nombre",self.nombre)



# bloque principal

persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()

persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()
