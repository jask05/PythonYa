"""
La lista es una estructura mutable (es decir podemos modificar sus elementos, agregar y borrar) 
en cambio una tupla es una secuencia de datos inmutable, es decir una vez definida no puede 
cambiar.

En general podemos crear y combinar tuplas con elementos de tipo lista y viceversa, es decir listas con componente tipo tupla.
"""

empleado=["juan", 53, (25, 11, 1999)]
print(empleado)
empleado.append((1, 1, 2016))
print(empleado)
alumno=("pedro",[7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)