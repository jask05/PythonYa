"""
Problema propuesto

Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""

class Agenda:

    def __init__(self):
        self.contactos = {}
        self.menu()

    def menu(self):
        opcion = 0
        while opcion != 5:
            print("1. Carga de un contacto en la agenda.")
            print("2. Listado completo de la agenda.")
            print("3. Consulta ingresando el nombre de la persona.")
            print("4. Modificación de su teléfono y mail.")
            print("5. Finalizar programa.")
            opcion = int(input("¿Qué opción escoges? "))
            if opcion < 1 or opcion > 5:
                print(">>> Por favor, escoge un valor entre 1 y 5.")

            if opcion == 1:
                self.cargacontacto()
            elif opcion == 2:
                self.listacompleta()
            elif opcion == 3:
                self.consulta()
            elif opcion == 4:
                self.modificatelefonoymail()

    def cargacontacto(self):
        repe = int(input("¿Cuántos contactos deseas cargar?"))
        x = 0
        while x < repe:
            print("--------------------")
            nombre = input("> Nombre: ")
            telf = int(input("> Telefóno: "))
            mail = input("> Email: ")
            print("--------------------")
            self.contactos[nombre] = (telf,mail)
            x = x + 1


    def listacompleta(self):
        for nombre in self.contactos:
            print("--------------------")
            print("Nombre: ", nombre)
            print("Teléfono: ", self.contactos[nombre][0])
            print("Email: ", self.contactos[nombre][1])
            print("--------------------")

    def consulta(self,nombre=''):
        if nombre=="":
            nombre = input("¿Qué nombre desea buscar?")

        if nombre in self.contactos:
            print("--------------------")
            print("Nombre: ", nombre)
            print("Teléfono: ", self.contactos[nombre][0])
            print("Email: ", self.contactos[nombre][1])
            print("--------------------")
        else:
            print(">>> No existe el contacto que busca.")

    def modificatelefonoymail(self):
        nombre = input("Nombre del perfil que desea modificar: ")
        if nombre in self.contactos:
            telefono = int(input(">>> Nuevo teléfono: "))
            email = input(">>> Nuevo email: ")
            self.contactos[nombre] = (telefono,email)
            self.consulta(nombre)
        else:
            print(">>> No existe el contacto que busca.")

agenda = Agenda()
