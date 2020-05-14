# -*- coding: utf-8 -*-

"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor o igual al valor ingresado.
"""


def carga(articulos):
    articulos = int(articulos)
    if articulos > 0:

        article = []
        price = []

        for x in range(articulos):
            a = input("Articulo: ")
            article.append(a)
            p = int(input("Precio: "))
            price.append(p)

    return article,price

def articulo_mayor(articulo,precio):
    tamano = len(articulo)
    pmayor = precio[0]
    amayor = ""
    for x in range(1,tamano):
        if precio[x] > pmayor:
            pmayor = precio[x]
            amayor = articulo[x]

    return pmayor, amayor

def importe(valor,articulo,precio):
    tamano = len(articulo)
    art = []
    prc = []
    for x in range(tamano):
        if precio[x] <= valor:
            art.append(articulo[x])
            prc.append(precio[x])

    return art,prc

articulos,precios = carga(5)
print("Articulos: ",articulos)
print("Precios: ",precios)
pmayor,amayor = articulo_mayor(articulos,precios)
print("El articulo:",amayor," es el mas caro. Su precio es:",pmayor)
imp = int(input("Ingrese un importe:"))
art,prc = importe(imp,articulos,precios)
print("Articulos que cuestan igual o menos de",imp,"euros:")
for x in range(len(art)):
    print("-> Articulo: ",art[x])
    print("-> Precio: ",prc[x])