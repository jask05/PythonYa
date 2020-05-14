#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problema 1:

Veamos con un ejemplo la sintaxis para redefinir el operador +. 
Crearemos una clase Cliente de un banco y redefiniremos el operador + para 
que nos retorne la suma de los depósitos de los dos clientes que estamos sumando.

-----
NOTA: Es muy importante tener en cuenta que debemos redefinir un operador matemático 
siempre y cuando haga nuestro programa más legible.
Debemos redefinir los operadores +,-,*,/ etc. solo para las clases que con solo leer 
su nombre el programador intuya que operación implementaría dicho operador.
-----

Definimos el método especial __add__ al que le llega como parámetro además de self un objeto.
El objeto que llega corresponde al que se encuentra luego del operador +, es decir clie2:

"""

class Cliente:

    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto

    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1200)
cli2=Cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)

