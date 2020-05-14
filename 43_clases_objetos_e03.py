"""
Una clase es una plantilla (molde), que define atributos (lo que conocemos como variables) y métodos
(lo que conocemos como funciones).

La clase define los atributos y métodos comunes a los objetos de ese tipo, pero luego, cada objeto tendrá
sus propios valores y compartirán las mismas funciones.

self:
sirve para referirse al objeto actual. Este mecanismo es necesario para
poder acceder a los atributos y métodos del objeto diferenciando, por ejemplo, una variable local mi_var
de un atributo del objeto self.mi_var.

Problemas propuestos

Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados.
Imprimir un mensaje si es mayor de edad (edad>=18)
"""

class Persona:

    def inicializar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mayor(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("Es menor de edad.")

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


persona = Persona()
persona.inicializar("Agustín", 28)
persona.mayor()
persona.imprimir()
persona2 = Persona()
persona2.inicializar("Mataulanio", 8)
persona2.mayor()
persona2.imprimir()
