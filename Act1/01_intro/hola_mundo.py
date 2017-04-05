a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
if a>(b+c) or b>(a+c) or c>(a+b):
	print("Ingrese un traingulo valido.")
elif a==b and b==c:
	print("Triangulo equilatero.")
elif a==b or b==c or a==c:
	print("Triangulo isoceles.")
else:
	print("Triangulo escaleno.")