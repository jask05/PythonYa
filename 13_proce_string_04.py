oracion = input("Ingrese su frase: ")
x = 0
i = 0
while x < len(oracion):
	if oracion[x] == " ":
		i = i + 1
	x = x + 1

print("Espacios en blanco:" , i)