a = float(input("digite um valor para 'A': "))
b = float(input("digite um valor para 'B': "))
c = float(input("digite um valor para 'C': "))
if c>a:
	d = a
	a = c
	c = d
elif b>a:
	d = a
	a = b
	b = d

if a>=(b+c):
	print("nao forma triangulo")

elif a**2 == b**2 + c**2:
	print ("triangulo retangulo")

elif a**2 > b**2 + c**2:
	print ("triangulo obtusangulo")
	if a==b==c:
		print ("triangulo equilatero")
	elif a==b or a==c or b==c:
		print ("triangulo isoceles")

elif a**2 < b**2 + c**2:
	print ("triangulo acutangulo")
	if a==b==c:
		print ("triangulo equilatero")
	elif a==b or a==c or b==c:
		print ("triangulo isoceles")


