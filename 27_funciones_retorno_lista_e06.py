"""
Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
3) Imprimir las dos listas generadas.
"""

def carga_numero(repeticion):
    if repeticion > 0:
        lista = []
        for x in range(repeticion):
            l = input("Ingrese un valor positivo o negativo:")
            lista.append(l)

    return lista

def positivonegativo(lista):
    positivo = []
    negativo = []
    for x in range(len(lista)):
        if lista[x] > 0:
            positivo.append(lista[x])
        elif lista[x] < 0:
            negativo.append(lista[x])

    return [positivo,negativo]

# Permite solicitar la carga de números
# numeros = carga_numero(10)

numeros = [10, -12, -23, -5, -2, 11111, 2222, 3333]
num = positivonegativo(numeros)
print("Numeros positivos: ",num[0])
print("Numeros negativos: ",num[1])