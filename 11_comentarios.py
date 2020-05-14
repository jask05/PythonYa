valor = int(input("Ingrese un valor del 1 al 10: "))
if valor >= 1 and valor <= 10:
	for x in range(12):
		print(valor,"x",x+1,"=", valor*(x+1)) 
else:
	print("El valor tiene que ser entre 1 y 10.")