#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Problema 2:

Desarrollar una clase llamada Lista, que permita pasar al método __init__ 
una lista de valores enteros.
Redefinir los operadores +,-,* y // con respecto a un valor entero.

-----
NOTA: Es muy importante tener en cuenta que debemos redefinir un operador matemático 
siempre y cuando haga nuestro programa más legible.
Debemos redefinir los operadores +,-,*,/ etc. solo para las clases que con solo leer 
su nombre el programador intuya que operación implementaría dicho operador.
"""

class Lista:

    def __init__(self, lista):
        self.lista=lista

    def imprimir(self):
        print(self.lista)

    def __add__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]+entero)
        return nueva

    def __sub__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]-entero)
        return nueva

    def __mul__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]*entero)
        return nueva

    def __floordiv__(self,entero):
        nueva=[]
        for x in range(len(self.lista)):
            nueva.append(self.lista[x]/entero)
        return nueva
    

# bloque principal

lista1=Lista([3,4,5])
lista1.imprimir()
print(lista1+10)
print(lista1-10)
print(lista1*10)
print(lista1//10)