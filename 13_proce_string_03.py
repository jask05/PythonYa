# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter "@".
email = input("Ingrese una dirección email: ")
contador = 0
x = 0

while x<len(email):
	if email[x]=="@":
		contador = contador + 1
	x = x + 1

if contador < 1:
	print("NO has introducido un email.")
elif contador == 1:
	print("Email correcto.")
else:
	print("Tu email tiene más de un @.")

agus = "AgUs"
print(agus)
print(agus.lower())
print(agus.upper())
print(agus.capitalize())