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

Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes métodos: inicializar
los atributos, imprimir el valor del lado mayor y otro método que muestre si es equilátero o no.
El nombre de la clase llamarla Triangulo.
"""

class Triangulo:
    def inicializar(self,lista):
        self.lista = lista

    def mayor(self):
        self.m = self.lista[0]
        for x in range(1,len(self.lista)):
            if self.lista[x] > self.m:
                self.m = self.lista[x]

        return self.m

    def tipo(self):
        self.m = self.lista[0]
        for x in range(1, len(self.lista)):
            if self.lista[x] == self.m:
                return "equilatero"
            else:
                return "NO es equilatero"

v1 = [5,5,5]
t1 = Triangulo()
t1.inicializar(v1)
print("Lado mayor:",t1.mayor())
print("Tipo:",t1.tipo())

v2 = [7,6,5]
t2 = Triangulo()
t2.inicializar(v2)
print("Lado mayor:",t2.mayor())
print("Tipo:",t2.tipo())