"""
Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. 
La segunda que solicite la carga de dos valores y muestre el producto de los mismos. 
LLamar desde el bloque del programa principal a ambas funciones.
"""

def cuadrado():
    valor = int(input("Número: "))
    resultado = valor * valor
    print("Su cuadrado es:",resultado)
    print("------------------------------")

def producto():
    v1 = int(input("Valor 1: "))
    v2 = int(input("Valor 2: "))
    rs = v1 * v2
    print("Producto: ",rs)
    print("------------------------------")

cuadrado()
producto()